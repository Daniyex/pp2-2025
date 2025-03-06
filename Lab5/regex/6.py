import re

def replace_space_comma_dot(text):
    return re.sub(r'[ ,.]', ':', text)
s = input()
print(replace_space_comma_dot(s)) 
