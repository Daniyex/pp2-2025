def palindrome():
    text = input().replace(" ","").lower()
    return text == text[::-1]

print(palindrome())
