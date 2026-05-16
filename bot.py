import telebot

TOKEN = "8894488238:AAFBcqMsg47CU3wRengom-zGWB37t3P29Xs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Working ✅")

print("Bot Running...")
bot.infinity_polling(skip_pending=True, none_stop=True)
