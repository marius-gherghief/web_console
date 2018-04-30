# coding: UTF-8

import logging
import logging.config
import sys
import time

from web_console.bot import Bot
from web_console import settings


def main():
    if settings.STARTUP_DELAY:
        time.sleep(int(settings.STARTUP_DELAY))
    else:
        time.sleep(10)

    logging.info("Starting service web_console...")

    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        logging.info('Stopping slack bot!')


if __name__ == "__main__":
    main()
