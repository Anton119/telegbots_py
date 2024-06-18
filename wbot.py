import telebot 
from telebot import types

bot = telebot.TeleBot("6682439921:AAGeBnYmrC_Y_RVDucJbtFElBgP-X277fuE")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет, я ВомбатуS - маленький', reply_markup=markup)
    file = open('./wb.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    
    
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url="https://www.google.ru/?hl=ru")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data="delete")
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data="edit")
    markup.row(btn2, btn3)
    bot.reply_to(message, "Какое красивое фото!", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)
     

bot.polling(none_stop=True)

