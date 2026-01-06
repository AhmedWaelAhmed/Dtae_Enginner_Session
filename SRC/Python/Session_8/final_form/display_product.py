from prettytable import PrettyTable

def display_table(data_list):
    # إنشاء الجدول
    table = PrettyTable()
    
    # تحديد أسماء العواميد
    table.field_names = ["Product Name", "Price ($)", "Quantity"]
    
    # ملء الجدول بالبيانات
    for item in data_list:
        table.add_row([
            item["name"], 
            f"{item['price']:.2f}",  # تنسيق السعر
            item["quantity"]
        ])
        
    print(table)