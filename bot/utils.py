import requests

def get_dollar_price():
    url = "http://api.navasan.tech/latest/?api_key=freetQ0Wd00VVBIlzUiVVNXdD2tFmfom"  # کلید API شما وارد شده است

    try:
        # ارسال درخواست به API
        response = requests.get(url)
        response.raise_for_status()  # بررسی موفقیت‌آمیز بودن درخواست

        # پردازش داده‌های JSON
        data = response.json()

        # استخراج قیمت خرید و فروش دلار هرات نقدی
        buy_price = data['harat_naghdi_buy']['value']
        sell_price = data['harat_naghdi_sell']['value']

        # بازگشت اطلاعات
        return f"قیمت خرید دلار: {buy_price} ریال\nقیمت فروش دلار: {sell_price} ریال"

    except requests.exceptions.RequestException as e:
        return f"خطا در ارتباط با سایت: {e}"
