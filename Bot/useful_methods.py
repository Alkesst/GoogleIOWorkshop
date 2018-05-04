from time import sleep

from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove

custom_keyboard = [['Opción 1', 'Opción 2'], ['Opción 3', 'Opción 4'], ['Done!']]
markup = ReplyKeyboardMarkup(custom_keyboard)


def arriba(bot, update):
    bot.send_message(chat_id=update.message.chat.id, text="Select your option!", reply_markup=markup)


def done(bot, update):
    reply_markup = ReplyKeyboardRemove()
    bot.send_message(chat_id=update.message.chat.id, text="Nice! :)", reply_markup=reply_markup)


def hello(bot, update):
    update.message.reply_text(f'Hello {update.message.from_user.first_name}')


def it_rocks(bot, update):
    update.message.reply_text(f'Yeeeah, Google I/O rocks!!!')


def start(bot, update):
    update.message.reply_text('Thanks for waking me up! I was bored with so much sleep :(')


def secret(bot, update, args):
    if ''.join(args) == "GoogleIO2018":
        bot.send_message(chat_id=update.message.chat_id, text='Now you can use super commands!')
    else:
        update.message.reply_text('Error! Wrong password!')


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(InlineQueryResultArticle(id=query.upper(), title='Caps',
                                            input_message_content=InputTextMessageContent(query.upper())))
    results.append(InlineQueryResultArticle(id=query.lower(), title='lower',
                                            input_message_content=InputTextMessageContent(query.lower())))
    bot.answer_inline_query(update.inline_query.id, results)


def echo_callback(bot, update, args):
    user_says = " ".join(args)
    update.message.reply_text("You said: " + user_says)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Eh...")
    sleep(1)
    bot.send_message(chat_id=update.message.chat_id, text="uhm...")
    sleep(2)
    bot.send_message(chat_id=update.message.chat_id, text="I'm sorry I don't understand that :(")
