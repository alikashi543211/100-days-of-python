def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a, b):
    if(a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass
a = 9
b = 8

# if(a > b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(a, b)

# gmean = (a * b)/(a + b) 
# print(gmean)
calculateGmean(a, b)

c = 8
d = 7
# gmean2 = (c * d)/(c + d)
# print(gmean2)
# if(c > d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(c, d)
calculateGmean(c, d)

