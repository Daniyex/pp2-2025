from functools import reduce

def multiply_list():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return reduce(lambda x, y: x * y, numbers, 1)

print(multiply_list())