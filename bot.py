import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id

    if uid not in users:
        users[uid] = 1000

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🎰 Казино", "👤 Профиль")
    markup.row("🎁 Бонус", "💎 Баланс")
    markup.row("🆘 Поддержка")

    bot.send_message(
        uid,
        "🖤💛 Добро пожаловать в TONPLAY!\n\n"
        "Твоё казино начинается здесь!",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text == "👤 Профиль")
def profile(message):
    bot.send_message(
        message.chat.id,
        f"👤 Твой ID: {message.from_user.id}"
    )

@bot.message_handler(func=lambda m: m.text == "💎 Баланс")
def balance(message):
    bot.send_message(
        message.chat.id,
        f"💎 Твой баланс: {users.get(message.from_user.id, 1000)} монет"
    )

@bot.message_handler(func=lambda m: m.text == "🎁 Бонус")
def bonus(message):
    users[message.from_user.id] = users.get(message.from_user.id, 1000) + 100
    bot.send_message(message.chat.id, "🎁 Ты получил 100 виртуальных монет!")

@bot.message_handler(func=lambda m: True)
def other(message):
    if message.text == "🎰 Казино":
        bot.send_message(message.chat.id, "🎰 Скоро здесь появятся игры!")

bot.infinity_polling()
