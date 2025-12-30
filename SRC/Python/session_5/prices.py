# pric.py

def g(amt):
    return amt * 0.10  # Returns 10% of amount

print("out of function") # This runs immediately when imported

if __name__ == "__main__":
    # This block ONLY runs if you execute 'python3 pric.py' directly
    print("Main file")