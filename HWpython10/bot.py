from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from logger import sring_to_list
from mult import multiply
from divis import division
from subst import substraction
from add import addition

TOKEN = "6097565598:AAFMivY9BEdh2THfJbXuz57Wg5uP8Mba4EA"
print('start')

A = 0
B = 1
C = 2

bot = Bot(token=TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def start(update:Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Привет я бот-калькулятор')
    context.bot.send_message(update.effective_chat.id, 'Если хочешь что-нибудь посчитать напиши "ДА", если не хочешь напиши "НЕТ"')
    return A

def user_answer(update:Update, context: CallbackContext):
    text = update.message.text
    if 'да' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Тогда начнем вычислять')
        context.bot.send_message(update.effective_chat.id, 'Напиши в сообщении математическое выражение например: "3+1*4/8"')
        return B
    else:
        context.bot.send_message(update.effective_chat.id, 'Не хочешь, как хочешь')
        context.bot.send_message(update.effective_chat.id, 'На этом моя работа окончена, пока!')
        return ConversationHandler.END

def calculator(update:Update, context: CallbackContext):  
    text = update.message.text
    express_list = sring_to_list(text)
    express_list = multiply(express_list)
    express_list = division(express_list)
    express_list = substraction(express_list)
    express_list = addition(express_list)

    log(update, context, express_list)

    context.bot.send_message(update.effective_chat.id, f'Результат выражения {text} равен {express_list[0]}')
    
    context.bot.send_message(update.effective_chat.id, 'Если хочешь продолжить вичисления напиши "ДА", если не хочешь напиши "НЕТ"')
    
    return C


def stop(update:Update, context: CallbackContext):
    text = update.message.text
    if 'да' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Напиши в сообщении математическое выражение например: "3+1*4/8"')
        return B
    else:
        context.bot.send_message(update.effective_chat.id, 'Не хочешь, как хочешь')
        context.bot.send_message(update.effective_chat.id, 'На этом моя работа окончена, пока!')
        return ConversationHandler.END
    
def log(update:Update, context: CallbackContext, express_list):
    with open('data_base.csv', 'a', encoding='utf-8') as data:
        data.write(f'{update.effective_user.first_name}, {update.effective_user.last_name}, {update.effective_user.id}, {update.message.text}, {str(express_list[0])}\n')

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Что-то пошло не так")


start_handler = CommandHandler('start', start)
user_answer_handler = MessageHandler(Filters.text, user_answer)
stop_handler = MessageHandler(Filters.text, stop)
calculator_handler = MessageHandler(Filters.text, calculator)
cancel_handler = CommandHandler('cancel', cancel)
menu_handler = ConversationHandler  (
                                    entry_points = [start_handler],
                                    states = {
                                        A: [user_answer_handler],
                                        B: [calculator_handler],
                                        C: [stop_handler],
                                        },
                                    fallbacks = [cancel_handler]
                                    )

dispatcher.add_handler(menu_handler)
dispatcher.add_handler(cancel_handler)

updater.start_polling()
updater.idle()