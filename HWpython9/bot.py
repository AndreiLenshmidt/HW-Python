from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from logger import start, user_answer, deleter, by, cancel

token1 = "6097565598:AAFMivY9BEdh2THfJbXuz57Wg5uP8Mba4EA"

bot = Bot(token="6097565598:AAFMivY9BEdh2THfJbXuz57Wg5uP8Mba4EA")
updater = Updater(token=token1)
dispatcher = updater.dispatcher

A = 0
B = 1
C = 2

start_handler = CommandHandler('start', start)
user_answer_handler = MessageHandler(Filters.text, user_answer)
deleter_handler = MessageHandler(Filters.text, deleter)
by_handler = MessageHandler(Filters.text, by)
cancel_handler = CommandHandler('cancel', cancel)

dialog_handler = ConversationHandler(
                                    entry_points = [start_handler],
                                    states = {
                                        A: [user_answer_handler],
                                        B: [deleter_handler],
                                        C: [by_handler]
                                        },
                                    fallbacks = [cancel_handler]
                                    )

dispatcher.add_handler(dialog_handler)

print('server start')

updater.start_polling()
updater.idle()