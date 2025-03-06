import re

def match_a_anything_b(text):
    return bool(re.fullmatch(r'a.*b', text))
c = input()
print(match_a_anything_b(c))  