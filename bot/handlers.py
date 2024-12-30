from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot.utils import get_dollar_price

def send_dollar_price(update: Update, context: CallbackContext) -> None:
    price = get_dollar_price()
    update.message.reply_text(f"قیمت دلار: {price}")

def main():
    # توکن بات خود را وارد کنید
    updater = Updater("YOUR_BOT_TOKEN")
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("price", send_dollar_price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
