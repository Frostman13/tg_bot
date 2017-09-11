# Импортируем нужные компоненты
import tg_bot_settings, astrology, word_handler, calc
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, date, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Подключаем лог
import logging
logging.basicConfig(format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='tg_bot.log'
                    )

# Приветствие
def start_bot(bot, update):
    start_text = """Привет, {}!\n\nЯ простой бот и понимаю только команды: {}
    """.format(update.message.chat.first_name,'/start /planet /wordcount')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(start_text)    
    with open('customers.txt', "a") as local_file:
        local_file.write('{};{};{};{}\n'.format(update.message.chat.id, update.message.chat.username,update.message.chat.first_name,update.message.chat.last_name))
        close(local_file)

# Созвездие
def planet_bot(bot, update, args):
    if update.message.text == '/planet':
        update.message.reply_text('Пример использования команды\r\n/planet Mercury\r\nНазвание планеты пишется на английском')
    update.message.reply_text('Созвездие: {}'.format(astrology.get_constellation_name(args[0])))  

# Подсчёт слов в строке
def wordcount_bot(bot, update, args):
    if update.message.text == '/wordcount':
        update.message.reply_text('Пример использования команды\r\n/wordcount "текст текст текст"\r\nТекст обязательно указывать в кавычках')
    else:
        message_text = update._effective_message.text[11:]
        update.message.reply_text(word_handler.word_count(message_text))

def chat_bot(bot, update):
    text=update.message.text
    if text in calc.CALC_SYMBOLS:
        response = calc.key_calc(text,update.message.chat.id)
        if response != 'calc_continue':
            update.message.reply_text(response)
            clear_keyboards(bot)
    elif text.strip()[-1] == "=":
        update.message.reply_text(calc.chat_calc(text))
    elif text == 'Esc':
        clear_keyboards(bot)
    else:
        update.message.reply_text(text)
    logging.info(text)

def calc_bot(bot, update, args):
    calc.clear_calc(update.message.chat.id)
    custom_keyboard = [['1', '2','3','/'], ['4', '5','6','*'],['7', '8','9','-'],['Esc', '0','+','=']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat.id, 
                    text="Используйте клавиатуру", 
                    reply_markup=reply_markup)

def clear_keyboards(bot):
    reply_markup = telegram.ReplyKeyboardRemove(remove_keyboard=True)
    bot.send_message(chat_id=update.message.chat.id,
                    text="Наберите новую команду: /start /planet /calc /wordcount",
                    reply_markup=reply_markup)



def main():
    updater = Updater(tg_bot_settings.TELEGRAM_API_KEY)
    
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, chat_bot))
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(CommandHandler("planet", planet_bot, pass_args=True))
    dp.add_handler(CommandHandler("calc", calc_bot, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount_bot, pass_args=True))


    dp.add_handler(CommandHandler("button", button_bot))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

    chat_id = update.message.chat.id

bot = telegram.Bot(tg_bot_settings.TELEGRAM_API_KEY)
# bot.sendMessage(chat_id,'Бот запущен. Команды: /start /planet /button',disable_notification=True)


# На будущее
# def button(bot, update):
#     query = update.callback_query

#     bot.edit_message_text(text="Selected option: %s" % query.data,
#                           chat_id=query.message.chat_id,
#                           message_id=query.message.message_id)

# def button_bot(bot,update):
#     keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
#                  InlineKeyboardButton("Option 2", callback_data='2'),
#                  InlineKeyboardButton("Option 3", callback_data='3'),
#                  InlineKeyboardButton("Option 4", callback_data='4')],

#                 [InlineKeyboardButton("Option 5", callback_data='5'),
#                 InlineKeyboardButton("Option 6", callback_data='6')]]

#     reply_markup = InlineKeyboardMarkup(keyboard)

#     update.message.reply_text('Please choose:', reply_markup=reply_markup)
#     update.message.reply_text(keyboard)


if __name__ == '__main__':  
    logging.info('Bot started')
    main()
