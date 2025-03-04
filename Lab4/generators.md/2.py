def even_numbers(n):
    for num in range(0, n + 1, 2):  
        yield str(num)  

n = int(input())

print(", ".join(even_numbers(n)))
