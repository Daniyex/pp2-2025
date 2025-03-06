import re

def find_lowercase_with_underscore(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)
c = input()

print(find_lowercase_with_underscore(c))
