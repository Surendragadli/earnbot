import telebot
from telebot import types

# =========================
# BOT TOKEN
# =========================
TOKEN = "8977490017:AAHfXQQVnRfOfBZ8aZfCSRsgHkcGXB97aJ8"

bot = telebot.TeleBot(TOKEN)

# =========================
# FORCE JOIN CHANNEL
# =========================
CHANNEL_USERNAME = "@Surendraearninghub"
CHANNEL_LINK = "https://t.me/Surendraearninghub"

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:

            show_main_menu(message)

        else:
            force_join(message)

    except:
        force_join(message)

# =========================
# FORCE JOIN MESSAGE
# =========================
def force_join(message):

    markup = types.InlineKeyboardMarkup()

    join_btn = types.InlineKeyboardButton(
        "📢 Join Channel",
        url=CHANNEL_LINK
    )

    check_btn = types.InlineKeyboardButton(
        "✅ Joined",
        callback_data="check_join"
    )

    markup.add(join_btn)
    markup.add(check_btn)

    bot.send_message(
        message.chat.id,
        """
⚠️ पहले हमारा चैनल जॉइन करो फिर बोट इस्तेमाल करो।
        """,
        reply_markup=markup
    )

# =========================
# CHECK JOIN
# =========================
@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):

    user_id = call.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:

            bot.answer_callback_query(
                call.id,
                "✅ Verification Successful"
            )

            show_main_menu(call.message)

        else:

            bot.answer_callback_query(
                call.id,
                "❌ पहले चैनल जॉइन करो"
            )

    except:

        bot.answer_callback_query(
            call.id,
            "⚠️ पहले चैनल जॉइन करो"
        )

# =========================
# MAIN MENU
# =========================
def show_main_menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton("💰 Balance")
    b2 = types.KeyboardButton("👥 Refer")

    b3 = types.KeyboardButton("💸 Withdrawal")
    b4 = types.KeyboardButton("🆘 Help")

    markup.row(b1, b2)
    markup.row(b3, b4)

    bot.send_message(
        message.chat.id,
        f"""
🔥 Welcome {message.from_user.first_name} 🔥

💸 Earn With Sandeep Bot 💸

✅ Refer & Earn
✅ Daily Updates
✅ Withdrawal System

🎉 Bot Successfully Started
        """,
        reply_markup=markup
    )

# =========================
# BALANCE
# =========================
@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):

    bot.send_message(
        message.chat.id,
        """
💰 Your Balance

₹0
        """
    )

# =========================
# REFER
# =========================
@bot.message_handler(func=lambda message: message.text == "👥 Refer")
def refer(message):

    user_id = message.from_user.id

    bot_username = bot.get_me().username

    ref_link = f"https://t.me/{bot_username}?start={user_id}"

    bot.send_message(
        message.chat.id,
        f"""
👥 Your Referral Link:

{ref_link}

🔥 Invite Friends & Earn More

📢 Channel:
{CHANNEL_LINK}

▶️ YouTube:
https://youtube.com/@gadliofficial?si=V-1AlS7JgAMuFKVM

📷 Instagram:
https://www.instagram.com/gadli_surendra
        """
    )

# =========================
# WITHDRAWAL
# =========================
@bot.message_handler(func=lambda message: message.text == "💸 Withdrawal")
def withdrawal(message):

    bot.send_message(
        message.chat.id,
        """
💸 Withdrawal Information

✅ Minimum Withdrawal: ₹100

📝 Contact Admin After Completing Target
        """
    )

# =========================
# HELP
# =========================
@bot.message_handler(func=lambda message: message.text == "🆘 Help")
def help_support(message):

    bot.send_message(
        message.chat.id,
        """
🆘 Support & Help

👤 Admin ID:
8771820206

📢 Channel:
https://t.me/Surendraearninghub

▶️ YouTube:
https://youtube.com/@gadliofficial

📷 Instagram:
https://www.instagram.com/gadli_surendra
        """
    )

# =========================
# BOT START
# =========================
print("Bot Running Successfully ✅")

bot.infinity_polling(skip_pending=True)
