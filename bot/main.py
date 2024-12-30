import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import asyncio

# بارگذاری متغیرهای محیطی
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
CHAT_ID_FILE = "chat_ids.txt"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# تابع برای ذخیره chat_id
def save_chat_id(chat_id: str):
    try:
        with open(CHAT_ID_FILE, "a") as file:
            file.write(f"{chat_id}\n")
    except Exception as e:
        logger.error(f"Error saving chat ID: {e}")

# تابع هندلر دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = str(update.effective_chat.id)
    save_chat_id(chat_id)
    await update.message.reply_html(
        rf"سلام {user.mention_html()}! به ربات قیمت دلار خوش آمدید."
    )

# تابع دریافت قیمت دلار
def get_dollar_price():
    try:
        url = f"https://api.example.com/price?apikey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("price", "نامشخص")
    except Exception as e:
        logger.error(f"Error fetching dollar price: {e}")
        return "خطا در دریافت قیمت."

# تابع ارسال قیمت دلار به کاربران
async def send_dollar_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_dollar_price()
    with open(CHAT_ID_FILE, "r") as file:
        chat_ids = file.readlines()
    for chat_id in chat_ids:
        chat_id = chat_id.strip()
        try:
            await context.bot.send_message(chat_id, text=f"قیمت دلار: {price} تومان")
        except Exception as e:
            logger.error(f"Error sending message to {chat_id}: {e}")

# تابع اصلی
async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dollar", send_dollar_price))

    # مدیریت اجرای polling
    await application.initialize()
    await application.start()
    try:
        await asyncio.Event().wait()  # منتظر دستور توقف بماند
    finally:
        await application.stop()
        await application.shutdown()

# اجرای برنامه
if __name__ == "__main__":
    asyncio.run(main())
