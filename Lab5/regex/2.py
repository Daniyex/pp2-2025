import re

def match_a_followed_by_two_or_three_b(text):
    return bool(re.fullmatch(r'ab{2,3}', text))

print(match_a_followed_by_two_or_three_b("abb"))  