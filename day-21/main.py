# def average(a, b , c = 1):
#     print("The average is ", (a + b + c) / 2)

# average(b=9)

# def name(fname, mname = "John", lname = "Whatson"):
#     print("Hello, ", fname, mname, lname)

# name("Amy", "Agrwal", "Jain")

# average(5, 6)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is ", sum / len(numbers))