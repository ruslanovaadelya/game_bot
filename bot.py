from config import TOKEN
from main import variant_game
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])

def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("🪨")
    b2 = types.KeyboardButton("✂️")
    b3 = types.KeyboardButton("📄")
    menu.add(b1,b2,b3)
    bot.send_message(message.chat.id,"Давай поиграем выбери: камень,ножницы или бумага",reply_markup=menu)


@bot.message_handler(content_types=['text'])
def second(message):
    if message.chat.type == "private":
        if message.text ==  "🪨":
            result = variant_game(1)  
            bot.send_message(message.chat.id,result)
        elif message.text == "✂️":
            result = variant_game(2)  
            bot.send_message(message.chat.id,result)
        elif message.text == "📄":
            result = variant_game(3)  
            bot.send_message(message.chat.id,result)
        else:
            bot.send_message(message.chat.id,"Выберите коректные данные")

bot.polling(non_stop=True)