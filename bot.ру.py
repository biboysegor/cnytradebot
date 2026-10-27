import telebot
from telebot import types

# 1. Вставьте сюда токен вашего бота @cnytrade_bot, полученный от @BotFather
TOKEN = "8580902159:AAFNTJAfIWibDwLcdjsZG2mtSfxM7Uy4lVU"

# 2. Вставьте сюда ссылку на ваш сайт, которую вы скопировали с Vercel
WEB_APP_URL = "https://cnytrade.surge.sh"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  web_app = types.WebAppInfo(url=WEB_APP_URL)
  markup.add(
      types.InlineKeyboardButton(
          "📈 Открыть калькулятор CNY/BYN", web_app=web_app
      )
  )

  bot.send_message(
      message.chat.id,
      "Привет! Это официальный бот @cnytrade_bot.\nНажми кнопку ниже,"
      " чтобы открыть мини-приложение для конвертации юаней и белорусских"
      " рублей:",
      reply_markup=markup,
  )

import os
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Запуск веб-сервера в отдельном потоке
threading.Thread(target=run_web, daemon=True).start()



if __name__ == "__main__":
  print("Бот @cnytrade_bot запущен и ожидает пользователей...")
  bot.infinity_polling()
