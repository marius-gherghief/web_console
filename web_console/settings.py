# -*- coding: utf-8 -*-

import os
import logging
from configparser import ConfigParser, NoOptionError
import paramiko

logging.basicConfig(level=logging.INFO)
paramiko.util.get_logger("paramiko").setLevel(logging.INFO)

DEBUG = True

PLUGINS = [
    'web_console.plugins',
]

ERRORS_TO = None

SSH_PORT = 22
SSH_USER = None
SSH_PASSWORD = None

# API_TOKEN = '###token###'

'''
Setup a comma delimited list of aliases that the bot will respond to.

Example: if you set ALIASES='!,$' then a bot which would respond to:
'botname hello'
will now also respond to
'$ hello'
'''
ALIASES = ''

'''
If you use Slack Web API to send messages (with
send_webapi(text, as_user=False) or reply_webapi(text, as_user=False)),
you can customize the bot logo by providing Icon or Emoji. If you use Slack
RTM API to send messages (with send() or reply()), or if as_user is True
(default), the used icon comes from bot settings and Icon or Emoji has no
effect.
'''
# BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
# BOT_EMOJI = ':godmode:'

'''Specify a different reply when the bot is messaged with no matching cmd'''
DEFAULT_REPLY = None

for key in os.environ:
    if key[:3] == 'WC_':
        name = key[3:]
        globals()[name] = os.environ[key]

config_path = os.path.join(os.getcwd(), 'config.ini')
if os.path.isfile(config_path):
    config_parser = ConfigParser(empty_lines_in_values=False)
    config_parser.optionxform = lambda s: s
    with open(config_path, "r") as config_file:
        config_parser.read_file(config_file)

    try:
        DEBUG = config_parser.getboolean("MAIN", "DEBUG")
        logging.debug("Using option %s = %s" % ("DEBUG", DEBUG))
        if DEBUG:
            logging.basicConfig(level=logging.DEBUG)
            paramiko.util.get_logger("paramiko").setLevel(logging.DEBUG)
    except NoOptionError:
        pass

    try:
        API_TOKEN = config_parser.get("MAIN", "API_TOKEN")
    except NoOptionError:
        pass

    try:
        DEFAULT_REPLY = config_parser.get("MAIN", "DEFAULT_REPLY")
        logging.debug("Using option %s = %s" % ("DEFAULT_REPLY", DEFAULT_REPLY))
    except NoOptionError:
        pass

    try:
        ERRORS_TO = config_parser.get("MAIN", "ERRORS_TO")
        logging.debug("Using option %s = %s" % ("ERRORS_TO", ERRORS_TO))
    except NoOptionError:
        pass

    try:
        plugins_config = config_parser.get("MAIN", "PLUGINS")
        PLUGINS = plugins_config.split(",")
        logging.debug("Using option %s = %s" % ("PLUGINS", PLUGINS))
    except NoOptionError:
        pass

    try:
        SSH_USER = config_parser.get("SSH", "USER")
        logging.debug("Using option %s = %s" % ("SSH_USER", SSH_USER))
    except NoOptionError:
        pass

    try:
        SSH_PASSWORD = config_parser.get("SSH", "PASSWORD")
    except NoOptionError:
        pass

    try:
        SSH_PORT = config_parser.getint("SSH", "PORT")
        logging.debug("Using option %s = %s" % ("SSH_PORT", SSH_PORT))
    except NoOptionError:
        pass

        logging.info("Successfully loaded config from ini file")
else:
    logging.error("Failed to locate the config file: %s" % config_path)

os.environ['WEBSOCKET_CLIENT_CA_BUNDLE'] = os.path.join(os.getcwd(), 'cacert.pem')
