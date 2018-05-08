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
    opt1 = message_filters.Opcion1()
    opt2 = message_filters.Opcion2()
    opt3 = message_filters.Opcion3()
    opt4 = message_filters.Opcion4()
    updater = Updater(token.get_token()["telegram"])
    updater.dispatcher.add_handler(CommandHandler("hello", useful_methods.hello))
    updater.dispatcher.add_handler(CommandHandler("start", useful_methods.start))
    updater.dispatcher.add_handler(CommandHandler("secret", useful_methods.secret, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("echo", useful_methods.echo_callback, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("menu", useful_methods.arriba))
    updater.dispatcher.add_handler(MessageHandler(done, useful_methods.done))
    updater.dispatcher.add_handler(MessageHandler(google_io, useful_methods.it_rocks))
    updater.dispatcher.add_handler(MessageHandler(opt1, useful_methods.option1))
    updater.dispatcher.add_handler(MessageHandler(opt2, useful_methods.option2))
    updater.dispatcher.add_handler(MessageHandler(opt3, useful_methods.option3))
    updater.dispatcher.add_handler(MessageHandler(opt4, useful_methods.option4))
    updater.dispatcher.add_handler(InlineQueryHandler(useful_methods.inline_caps))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, useful_methods.unknown))
    print("Bot running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Preparing bot...")
    main()
