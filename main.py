from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

TOKEN = "5592811247:AAE_bbQOmxE0HqWn8dLe7By90atR5IICZKs"

def echo(update, context):
    txt = update.message.text
    if txt.lower() in['привет', 'здаров']:
        txt = "И тебе привет бедолага!"
    update.message.reply_text(txt)

def start(update, context):
    update.message.reply_text("Это учебный эхобот.\nДля вызова помощи наберите /help")

def start(update, context):
    update.message.reply_text("Для вызова помощи наберите /help\nдля поиска в википедии /wiki <текст для поиска>")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен...")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()