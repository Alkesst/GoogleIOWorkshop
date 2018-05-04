# made by Alkesst using python3.6 and python-telegram-bot
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler, Filters
from Bot import useful_methods, message_filters, token

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    google_io = message_filters.GoogleIOFilter()
    done = message_filters.Done()
    # updater = Updater(token.get_token()["telegram"])
    updater = Updater("526743804:AAHMrCsJ5j6dwsBeljlq1yIlvCfktQs6ujI")
    updater.dispatcher.add_handler(CommandHandler("hello", useful_methods.hello))
    updater.dispatcher.add_handler(CommandHandler("start", useful_methods.start))
    updater.dispatcher.add_handler(CommandHandler("secret", useful_methods.secret, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("echo", useful_methods.echo_callback, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("menu", useful_methods.arriba))
    updater.dispatcher.add_handler(MessageHandler(done, useful_methods.done))
    updater.dispatcher.add_handler(MessageHandler(google_io, useful_methods.it_rocks))
    updater.dispatcher.add_handler(InlineQueryHandler(useful_methods.inline_caps))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, useful_methods.unknown))
    print("Bot running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Preparing bot...")
    main()
