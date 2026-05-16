import telebot
from telebot import types

TOKEN = "8894488238:AAFom771RgGEoPb_Wk8jBlxPtIBPW3fu8_g"

bot = telebot.TeleBot(TOKEN)

# START COMMAND
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton("💰 Balance")
    b2 = types.KeyboardButton("👥 Refer")
    b3 = types.KeyboardButton("💸 Withdrawal")
    b4 = types.KeyboardButton("🆘 Help")

    markup.row(b1, b2)
    markup.row(b3, b4)

    bot.send_message(
        message.chat.id,
        f"🔥 Welcome {message.from_user.first_name} 🔥\n\nEarn With Gadli Bot Working ✅",
        reply_markup=markup
    )

# BALANCE
@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):
    bot.send_message(message.chat.id, "💰 Your Balance: ₹0")

# REFER
@bot.message_handler(func=lambda message: message.text == "👥 Refer")
def refer(message):

    user_id = message.from_user.id
    username = bot.get_me().username

    ref_link = f"https://t.me/{username}?start={user_id}"

    bot.send_message(
        message.chat.id,
        f"👥 Your Referral Link:\n\n{ref_link}"
    )

# WITHDRAWAL
@bot.message_handler(func=lambda message: message.text == "💸 Withdrawal")
def withdrawal(message):
    bot.send_message(
        message.chat.id,
        "💸 Minimum withdrawal ₹100"
    )

# HELP
@bot.message_handler(func=lambda message: message.text == "🆘 Help")
def help_msg(message):
    bot.send_message(
        message.chat.id,
        "🆘 Contact Admin: @yourusername"
    )

print("Bot Working ✅")

bot.infinity_polling(skip_pending=True)
