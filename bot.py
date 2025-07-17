import telebot
from telebot import types

# ✅ তোমার টোকেন এখানে বসাও
bot = telebot.TeleBot("8076079517:AAEXjueSO88xjAIzdceg8Wv_cEy4qaEFWD4")
print("✅ Bot is running...")

# ▶️ Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🎓 About Us", "📞 Contact")
    markup.row("🌐 Website", "▶️ YouTube")
    
    welcome_text = (
        "👋 **Welcome to Pathsala Vidyapith!**\n\n"
        "📚 An educational platform built for learners like you.\n\n"
        "Type /help to explore more options."
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# ❓ Help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🤖 I can assist you with the following:\n\n"
        "👉 /start - Show main menu\n"
        "👉 /help - Show this help message\n\n"
        "Or use the buttons below to explore more!"
    )
    bot.send_message(message.chat.id, help_text)

# 🔁 Message handler for custom replies
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    text = message.text.lower()

    if "about" in text or "🎓" in text:
        bot.reply_to(message, 
            "📖 *Pathsala Vidyapith* is an online & offline education platform that offers free and premium courses.\n\n"
            "We aim to bring quality education to all learners.\n\n"
            "Visit our website or YouTube channel to learn more!",
            parse_mode='Markdown'
        )
    elif "contact" in text or "📞" in text:
        bot.reply_to(message, 
            "📞 Helpline: 6295319996\n📧 Email: support@pathsalavidyapith.in"
        )
    elif "website" in text or "🌐" in text:
        bot.reply_to(message, 
            "🌐 Visit our official website:\nhttps://www.pathsalavidyapith.in/"
        )
    elif "youtube" in text or "▶️" in text:
        bot.reply_to(message, 
            "▶️ Subscribe to our YouTube channel:\nhttps://www.youtube.com/@PathsalaVidyapith"
        )
        import os
     if __name__ == "__main__":
        bot.remove_webhook()
        bot.set_webhook(url='https://your-app-name.onrender.com/')
        port = int(os.environ.get("PORT", 5000))  # Render দিয়া পোর্ট নিবে
        app.run(host="0.0.0.0", port=port)


# ▶️ Run the bot
print("✅ Bot is running...")
bot.polling()
