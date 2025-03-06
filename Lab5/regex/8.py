import re

def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)
s = input()
print(split_at_uppercase(s))  
