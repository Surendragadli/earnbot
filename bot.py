import telebot

TOKEN = "8894488238:AAGGYuftUkRlOHXRl3XuAm0nnhK9X7tdiAg"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Working ✅")

print("Bot Running...")
bot.infinity_polling()