# made by Alkesst using python3.6 and python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler
from Bot import useful_methods, message_filters, token


def main():
    google_io = message_filters.GoogleIOFilter()
    updater = Updater(token.get_token()["telegram"])
    updater.dispatcher.add_handler(CommandHandler("hello", useful_methods.hello))
    updater.dispatcher.add_handler(CommandHandler("start", useful_methods.start))
    updater.dispatcher.add_handler(CommandHandler("secret", useful_methods.secret, pass_args=True))
    updater.dispatcher.add_handler(MessageHandler(google_io, useful_methods.it_rocks))
    updater.dispatcher.add_handler(InlineQueryHandler(useful_methods.inline_caps))
    print("Bot running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Preparing bot...")
    main()
