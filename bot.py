import telebot
from telebot import types

# =========================
# BOT TOKEN
# =========================
TOKEN = "8977490017:AAHfXQQVnRfOfBZ8aZfCSRsgHkcGXB97aJ8"

bot = telebot.TeleBot(TOKEN)

# =========================
# =========================
# FORCE JOIN MESSAGE
# =========================
def force_join(message):

    markup = types.InlineKeyboardMarkup()

    ch1_btn = types.InlineKeyboardButton(
        "📢 Channel 1",
        url="https://t.me/Surendraearninghub"
    )

    ch2_btn = types.InlineKeyboardButton(
        "📢 Channel 2",
        url="https://t.me/surendraquizhub"
    )

    yt_btn = types.InlineKeyboardButton(
        "▶️ YouTube",
        url="https://youtube.com/@gadliofficial?si=V-1AlS7JgAMuFKVM"
    )

    insta_btn = types.InlineKeyboardButton(
        "📷 Instagram",
        url="https://www.instagram.com/gadli_surendra?igsh=MTUzZWZiOGszeTNxMg=="
    )

    check_btn = types.InlineKeyboardButton(
        "✅ Verify Joined",
        callback_data="check_join"
    )

    markup.add(ch1_btn)
    markup.add(ch2_btn)
    markup.add(yt_btn, insta_btn)
    markup.add(check_btn)

    bot.send_message(
        message.chat.id,
        """
⚠️ पहले नीचे दिए गए सभी चैनल और सोशल मीडिया जॉइन / फॉलो करो फिर Verify पर क्लिक करो।
        """,
        reply_markup=markup
    )
# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    markup = types.InlineKeyboardMarkup()

    ch1 = types.InlineKeyboardButton(
        "📢 Channel 1",
        url="https://t.me/Surendraearninghub"
    )

    ch2 = types.InlineKeyboardButton(
        "📢 Channel 2",
        url="https://t.me/surendraquizhub"
    )

    yt = types.InlineKeyboardButton(
        "▶️ YouTube",
        url="https://youtube.com/@gadliofficial?si=V-1AlS7JgAMuFKVM"
    )

    insta = types.InlineKeyboardButton(
        "📷 Instagram",
        url="https://www.instagram.com/gadli_surendra?igsh=MTUzZWZiOGszeTNxMg=="
    )

    verify = types.InlineKeyboardButton(
        "✅ Verify Joined",
        callback_data="verify_join"
    )

    markup.add(ch1)
    markup.add(ch2)
    markup.add(yt, insta)
    markup.add(verify)

    bot.send_message(
        message.chat.id,
        f"""
🔥 Welcome {message.from_user.first_name} 🔥

🎁 Join All Channels & Get ₹45 Bonus

⚠️ पहले सभी चैनल Join करो फिर Verify Joined दबाओ
        """,
        reply_markup=markup
    )
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
# =========================
# VERIFY JOIN
# =========================
@bot.callback_query_handler(func=lambda call: call.data == "verify_join")
def verify_join(call):

    user_id = call.from_user.id

    try:
        ch1 = bot.get_chat_member("@Surendraearninghub", user_id)

        if ch1.status in ["member", "administrator", "creator"]:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            b1 = types.KeyboardButton("💰 Balance")
            b2 = types.KeyboardButton("👥 Refer")
            b3 = types.KeyboardButton("💸 Withdrawal")
            b4 = types.KeyboardButton("🆘 Help")

            markup.row(b1, b2)
            markup.row(b3, b4)

            bot.send_message(
                call.message.chat.id,
                """
✅ Verification Successful

🎁 ₹45 Joining Bonus Added

🚀 Bot Activated Successfully
                """,
                reply_markup=markup
            )

        else:

            bot.answer_callback_query(
                call.id,
                "❌ पहले सभी चैनल Join करो"
            )

    except:

        bot.answer_callback_query(
            call.id,
            "⚠️ पहले चैनल Join करो"
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

# =========================
# BOT START
# =========================
print("Bot Running Successfully ✅")

bot.infinity_polling(skip_pending=True)
