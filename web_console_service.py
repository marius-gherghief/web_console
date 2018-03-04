# coding: UTF-8

import logging
import logging.config
import sys

from web_console.bot import Bot
from web_console import settings


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

    logging.info("Starting service web-console...")

    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        logging.info('Stopping slack bot!')


if __name__ == "__main__":
    main()
