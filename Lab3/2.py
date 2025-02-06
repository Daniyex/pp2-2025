def convtemp(f):
    c = (5/9)*(f-32)
    return c

f = int(input())
c = convtemp(f)
print(c)