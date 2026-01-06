import random
import json

def log():
    print("--- Login System Started ---")
    
    # محاولة قراءة ملف المستخدمين
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        print("Error: users.json file not found!")
        return False

    while True:
        x = input("Enter your username: ")
        
        if x in users_data:
            y = input("Enter your password: ") 
            
            if y == users_data[x]:
                s = random.randrange(1000, 10000)
                print(f"Verification code is: {s}")
                
                while True:
                    try:
                        L = int(input("Enter verification code: "))
                        if L == s:
                            print("\n>>> Access Granted! Welcome. <<<\n")
                            return True # نرجع True عشان نقول للبرنامج يكمل
                        else:
                            print("Invalid verification code.")
                    except ValueError:
                        print("Please enter numbers only.")
            else:
                print("Incorrect Password")
        else:
            print("Invalid Username")