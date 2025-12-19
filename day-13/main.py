# Strings are immutable in python
a = "!!Harry!!!! !!!!!!!!!!!!!!! Akash"

print(len(a))

print(a.upper())

print(a.lower())

print(a.rstrip("!"))

print(a.replace("Harry", "John"))

print(a.split(' '))

blogHeading = "introduction to jS"

print(blogHeading.capitalize())

print(blogHeading)

str1 = "Welcome to the Console!!!"

print(len(str1))
print(len(str1.center(50)))

print(a.count("Harry"))

str1 = "WelcometotheConsole3400"
print(str1.endswith("!!!"))

print(str1.endswith("to", 4, 10))

print(str1.find('to0'))

print(str1.find('to'))

print(str1.index("to"))

print(str1.isalnum())

str1 = "Welcome"

print(str1.isalpha())

print(str1.islower())

str1 = "Welcome to house\n"

print(str1.isprintable())

b = "           "

print(b.isspace())


str1 = "World Health organization"
print(str1.istitle())

print(str1.startswith("World"))

print(str1.swapcase())