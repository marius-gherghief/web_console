import logging
import re
import threading
import time
from os.path import expanduser

import paramiko
import requests

from web_console import settings
from web_console.singleton import Singleton


class SlackSSHManager(Singleton):
    def __init__(self):
        self.ssh_user = None
        self.ssh_password = None
        self.ssh_port = 22
        self.ssh_clients = dict()
        self.initialized = False

    def initialize_shell(self, ssh_user, ssh_password, ssh_port):
        if not self.initialized:
            self.initialized = True
            self.ssh_user = ssh_user
            self.ssh_password = ssh_password
            self.ssh_port = ssh_port

    def get_session(self, message):
        user = message.body.get('user', '')
        if not user:
            user = message.body.get('username', '')
            # if not user:
            #     user = message.body['channel']
        user = user + message.body['channel']

        sh = None
        if user in self.ssh_clients:
            sh = self.ssh_clients[user]
            logging.info("Found ssh session: Closed = %s" % sh.closed)
            if not sh.closed:
                # sh.message = message
                return sh

        if sh:
            logging.info("Removing closed client: %s" % str(sh))
            del self.ssh_clients[user]

        sh = ShellHandler(host='127.0.0.1', user=self.ssh_user, psw=self.ssh_password, port=self.ssh_port, msg=message)

        logging.info("Adding new bash session for user: %s" % user)
        self.ssh_clients[user] = sh

        return sh

    def delete_session(self, message):
        user = message.body.get('user', '')
        if not user:
            user = message.body.get('username', '')
            # if not user:
            #     user = message.body['channel']
        user = user + message.body['channel']
        del self.ssh_clients[user]


class ShellHandler:

    def __init__(self, host, user, psw, port, msg):
        # logging.info("Data used: user=%s, pwd=%s" % (user, psw))
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, username=user, password=psw, port=port)
        self.home = expanduser("~")
        self.channel = self.ssh.invoke_shell()  # term='cygwin'
        self._message = msg

        self.reader = threading.Thread(target=self.read)
        self.reader.start()
        self._closed = False
        logging.info("home dir: %s." % self.home)

    def __del__(self):
        if self.ssh:
            self.ssh.close()

    def read(self):
        while True:
            if self.channel.recv_ready():
                data = '\t'.join(self.channel.recv(200).decode("utf-8").split('    '))
                chat_data = re.compile(r'\x1b[^m]*m')
                # logging.info("RAW data: %s" % data)
                self._message.reply(chat_data.sub('', data))
                # self._message.reply(data)
            time.sleep(0.3)

    def execute(self, cmd, no_enter=False):
        if not self.channel.closed:
            logging.info("Executing command: %s" % cmd)
            if no_enter:
                self.channel.send(cmd, )
            else:
                self.channel.send(cmd + '\n')

    def execute_download(self, message):
        url = message.body['file']['url_private_download']
        logging.info("Executing download: %s" % url)
        name = message.body['file']['name']
        r = requests.get(url, headers={'Authorization': 'Bearer %s' % settings.API_TOKEN}, stream=True)
        if r.status_code == 200:
            with open(self.home + '/' + name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            message.reply("File saved to: %s%s%s." % (self.home, '/', name))

    @property
    def message(self):
        return self._message

    # @message.setter
    # def message(self, value):
    #     self._message = value

    @property
    def closed(self):
        return self._closed or self.channel.closed

    @closed.setter
    def closed(self, value):
        self._closed = value
        if value:
            self.channel.close()


logging.info("Starting SSH Manager for user: %s, password: %s and port: %s" % (settings.SSH_USER,
                                                                               settings.SSH_PASSWORD,
                                                                               settings.SSH_PORT))
_ssh_manager = SlackSSHManager()
_ssh_manager.initialize_shell(settings.SSH_USER, settings.SSH_PASSWORD, settings.SSH_PORT)

# paramiko.util.log_to_file('slack_ssh_client.log')


def get_ssh_manager():
    return _ssh_manager
