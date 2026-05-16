import telebot

TOKEN = "8894488238:AAFom771RgGEoPb_Wk8jBlxPtIBPW3fu8_g"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Working ✅")

bot.infinity_polling(skip_pending=True)
