import re

def insert_spaces_in_camel_case(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
s = input()
print(insert_spaces_in_camel_case(s))  