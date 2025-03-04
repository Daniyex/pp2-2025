def countdown(n):
    for num in range(n, -1, -1):  
        yield num  

n = int(input())

for number in countdown(n):
    print(number)
