def count_case_letters():
    text = input("Enter a string: ")
    upper_case_count = sum(1 for char in text if char.isupper())
    lower_case_count = sum(1 for char in text if char.islower())
    print(f"Upper case letters: {upper_case_count}")
    print(f"Lower case letters: {lower_case_count}")

count_case_letters()
