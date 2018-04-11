# coding: UTF-8
import re

from web_console.bot import listen_to
from web_console.bot import respond_to

from web_console.ssh_manager import get_ssh_manager

ssh_man = get_ssh_manager()


@listen_to('ssh .*', re.IGNORECASE)
def ssh_reply(message):
    cmd = message.body['text']
    cmd = cmd[cmd.find('ssh ') + 4:]

    sh = ssh_man.get_session(message)

    sh.execute(cmd)


@respond_to('.*', re.IGNORECASE)
def ssh_reply(message):
    cmd = message.body['text']
    if cmd.lower().startswith('attach '):
        return

    if cmd.lower().startswith('key '):
        return

    sh = ssh_man.get_session(message)

    if 'subtype' in message.body and message.body['subtype'].lower().startswith('file_share'.lower()):
        sh.execute_download(message)
        return

    sh.execute(cmd)


@respond_to('key .*', re.IGNORECASE)
def ssh_key_commands(message):
    cmd = message.body['text']

    sh = ssh_man.get_session(message)

    if 'ctrl+c' in cmd.lower() or 'control+c' in cmd.lower():
        sh.execute(chr(3), no_enter=True)
    elif 'ctrl+x' in cmd.lower() or 'control+x' in cmd.lower():
        sh.execute(chr(24), no_enter=True)
    elif 'ctrl+z' in cmd.lower() or 'control+z' in cmd.lower():
        sh.execute(chr(26), no_enter=True)
    else:
        cmd = cmd[cmd.find('key ') + 4:]
        if cmd.isdigit():
            sh.execute(chr(int(cmd)), no_enter=True)
        else:
            sh.execute(cmd, no_enter=True)


@respond_to('attach .*', re.IGNORECASE)
@listen_to('attach .*', re.IGNORECASE)
def attach_reply(message):
    cmd = message.body['text']
    cmd = cmd[cmd.find('attach ') + 7:]
    message.channel.upload_file('', cmd.strip())
