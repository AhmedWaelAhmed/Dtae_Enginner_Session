# 1. استدعاء الملفات اللي عملناها
from login_sys import log
from display_product import display_table

# 2. تعريف البيانات (الداتا)
products = [
    {"name": "Water", "price": 80.0, "quantity": 1500},
    {"name": "Soda",  "price": 130.0, "quantity": 1500},
    {"name": "Chips", "price": 75.0,  "quantity": 1500},
    {"name": "Eggs",  "price": 200.0, "quantity": 1500},
]

# 3. تشغيل البرنامج (نقطة البداية)
if __name__ == "__main__":
    
    # أولاً: شغل نظام الدخول
    is_logged_in = log()
    
    # ثانياً: لو الدخول نجح، اعرض المنتجات
    if is_logged_in == True:
        print("Loading Product Data...")
        display_table(products)
    else:
        print("System Exited.")