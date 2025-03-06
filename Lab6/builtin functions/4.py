import time
import math

def delayed_square_root():
    number = int(input("Enter the number: "))
    delay = int(input("Enter delay in milliseconds: "))
    time.sleep(delay / 1000)  
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

delayed_square_root()