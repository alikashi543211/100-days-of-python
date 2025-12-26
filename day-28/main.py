letters = "Hey my name is {1} and I am from {0}"
country = "Pakistan"
name = "Kashif"

print(letters.format(country, name))

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.54321
txt = f"For only {price:21} dollars"
# print(txt.format(price = 49.45544))
print(txt)


print(type(f"{3*30}"))