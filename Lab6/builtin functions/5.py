def all_elements_true():
    values = tuple(map(bool, input("Enter tuple elements separated by space: ").split()))
    print(all(values))

all_elements_true()