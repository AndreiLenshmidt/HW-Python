from telegram.ext import ConversationHandler

A = 0
B = 1
C = 2

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, я удаляю все слова, где есть "абв"')
    context.bot.send_message(update.effective_chat.id, 'Напиши "да" если хочешь меня проверить')
    return A

def user_answer(update, context):
    text = update.message.text
    if 'да' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Напиши свою строку')
        return B
    else:
        context.bot.send_message(update.effective_chat.id, 'Не хочешь, как хочешь')
        context.bot.send_message(update.effective_chat.id, 'На этом моя работа окончена, пока!')
        return ConversationHandler.END

def deleter(update, context):
    context.bot.send_message(update.effective_chat.id, 'Я удалил, все что до чего смог добраться, вот результат:')
    text = update.message.text
    words = text.split()
    for i in words:
        if 'абв' in i.lower():
            words.remove(i)
    text = " ".join(words)
    context.bot.send_message(update.effective_chat.id, text)
    return C

def by(update, context):
    context.bot.send_message(update.effective_chat.id, 'На этом моя работа окончена, пока!')
    return ConversationHandler.END

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Что-то пошло не так")