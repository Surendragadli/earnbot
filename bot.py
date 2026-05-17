import telebot
from telebot import types

TOKEN = "8894488238:AAFom771RgGEoPb_Wk8jBlxPtIBPW3fu8_g"

bot = telebot.TeleBot(TOKEN)
# START COMMAND
@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    channel_username = "@Surendraearninghub"

    try:
        member = bot.get_chat_member(channel_username, user_id)

        if member.status in ["member", "administrator", "creator"]:

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

        else:
            raise Exception()

    except:

        join_markup = types.InlineKeyboardMarkup()

        join_btn = types.InlineKeyboardButton(
            "📢 Join Channel",
            url="https://t.me/Surendraearninghub"
        )

        check_btn = types.InlineKeyboardButton(
            "✅ Joined",
            callback_data="check_join"
        )

        join_markup.add(join_btn)
        join_markup.add(check_btn)

        bot.send_message(
            message.chat.id,
            "⚠️ पहले हमारा चैनल जॉइन करो फिर बोट यूज़ करो",
            reply_markup=join_markup
        )


@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):

    user_id = call.from_user.id
    channel_username = "@Surendraearninghub"

    try:
        member = bot.get_chat_member(channel_username, user_id)

        if member.status in ["member", "administrator", "creator"]:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            b1 = types.KeyboardButton("💰 Balance")
            b2 = types.KeyboardButton("👥 Refer")
            b3 = types.KeyboardButton("💸 Withdrawal")
            b4 = types.KeyboardButton("🆘 Help")

            markup.row(b1, b2)
            markup.row(b3, b4)

            bot.send_message(
                call.message.chat.id,
                "✅ Verification Successful\n\nBot Started Successfully",
                reply_markup=markup
            )

        else:
            bot.answer_callback_query(
                call.id,
                "❌ पहले चैनल जॉइन करो"
            )

    except:
        bot.answer_callback_query(
            call.id,
            "❌ पहले चैनल जॉइन करो"
        )


# BALANCE
@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):
    bot.send_message(message.chat.id, "💰 Your Balance: ₹0")


# REFER
@bot.message_handler(func=lambda message: message.text == "👥 Refer")
def refer(message):

    user_id = message.from_user.id

    ref_link = f"https://t.me/Earnwithgadli_bot?start={user_id}"

    text = f"""
👥 Your Referral Link:

{ref_link}

🔥 Earn With Gadli 🔥
💸 Daily Earn & Referral Bonus
⚡ Instant Updates
📈 Grow With Gadli

📢 Channel 1:
https://t.me/Surendraearninghub

📢 Channel 2:
https://t.me/surendraquizhub

▶️ YouTube:
https://youtube.com/@gadliofficial?si=V-1AlS7JgAMuFKVM

📷 Instagram:
https://www.instagram.com/gadli_surendra?igsh=MTUzZWZiOGszeTNxMg==
"""

    bot.send_message(message.chat.id, text)


# WITHDRAWAL
@bot.message_handler(func=lambda message: message.text == "💸 Withdrawal")
def withdrawal(message):
    bot.send_message(
        message.chat.id,
        "💸 Minimum withdrawal ₹100"
    )


# HELP
@bot.message_handler(func=lambda message: message.text == "🆘 Help")
def help_support(message):
    bot.send_message(
        message.chat.id,
        "🆘 Contact Admin:\n\n👤 Admin ID: 8771820206"
    )
