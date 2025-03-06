import re

def match_a_followed_by_b(text):
    return bool(re.fullmatch(r'a*b*', text))

print(match_a_followed_by_b("abbb"))  
