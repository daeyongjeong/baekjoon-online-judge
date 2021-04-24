a = int(input())
b = int(input())
for i in range(0, 3):
    print(a*((b % (10**(i+1)))//(10**i)))
print(a*b)
