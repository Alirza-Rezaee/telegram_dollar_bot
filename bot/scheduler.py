import schedule
import time
from telegram import Bot
from bot.utils import get_dollar_price

# توکن بات تلگرام خود را وارد کنید
TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"  # شناسه چت تلگرام خود را وارد کنید

def send_scheduled_price():
    bot = Bot(token=TOKEN)
    price = get_dollar_price()
    bot.send_message(chat_id=chat_id, text=f"قیمت دلار: {price}")

# زمان‌بندی ارسال پیام‌ها
schedule.every().day.at("06:00").do(send_scheduled_price)  # ساعت 6 صبح
schedule.every().day.at("12:00").do(send_scheduled_price)  # ساعت 12 ظهر
schedule.every().day.at("18:00").do(send_scheduled_price)  # ساعت 6 عصر
schedule.every().day.at("00:00").do(send_scheduled_price)  # ساعت 12 شب

# اجرای زمان‌بندی
while True:
    schedule.run_pending()
    time.sleep(60)  # بررسی هر 60 ثانیه برای زمان‌بندی
