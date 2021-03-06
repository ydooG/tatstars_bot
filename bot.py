import logging

from telegram.ext import Updater, Dispatcher, CommandHandler

from callbacks import go, ping, help, ramil
from constants import BOT_TOKEN, PORT, DEBUG, LOG_FORMAT, HEROKU_APP_NAME
from helpers import Database

database = Database()


def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher: Dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(command='go', callback=go))
    dispatcher.add_handler(CommandHandler(command='ping', callback=ping))
    dispatcher.add_handler(CommandHandler(command='ramil', callback=ramil))
    dispatcher.add_handler(CommandHandler(command='help', callback=help))

    if DEBUG:
        logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
        updater.start_polling()
    else:
        logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
        logging.info(str(PORT))
        updater.start_webhook(
            listen='0.0.0.0',
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f'https://{HEROKU_APP_NAME}.herokuapp.com/{BOT_TOKEN}'
        )
    updater.idle()


if __name__ == '__main__':
    main()
