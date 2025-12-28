def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(3))
print(factorial(4))
print(factorial(5))

f0 = 0
f1 = 1
f2 = f1 + f0 
# f(n) = f(n - 1) + f(n - 2)

def febnocci(n):
    if(n == 0):
        return 0
    elif( n == 1):
        return 1
    else:
        return febnocci(n - 1) + febnocci(n - 2)

print(febnocci(6))
