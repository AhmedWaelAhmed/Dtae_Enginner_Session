import random

def log():
    # Variables are now inside the function (local variables)
    u = "test"
    p = "1111"
    
    print("--- Login System Started ---")
    
    while True:
        x = input("Enter your username: ")
        
        if x == u:
            y = input("Enter your password: ") 
            
            if y == p:
                # Generates a number between 1000 and 9999
                s = random.randrange(1000, 10000)
                print("Verification code is:", s)
                
                while True:
                    try:
                        # Added int conversion safety
                        L = int(input("Enter verification code: "))
                        if L == s:
                            print("Access Granted")
                            return  # 'return' stops the function completely
                        else:
                            print("Invalid verification code : please define again")
                    except ValueError:
                        print("Please enter numbers only.")
            else:
                print("Incorrect Password")
                continue
        else:
            print("Invalid Username")
            continue
log()