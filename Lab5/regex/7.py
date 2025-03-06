import re

def snake_to_camel(text):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(text.split('_')))
s = input()
print(snake_to_camel(s))  