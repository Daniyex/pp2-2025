def squares(a, b):
    for num in range(a, b + 1):  
        yield num ** 2 

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)
