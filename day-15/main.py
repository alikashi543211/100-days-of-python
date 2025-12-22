import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime("%H")
if(int(timestamp) > 5 and int(timestamp) < 12):
    print("Good Morning")
elif(int(timestamp) > 12 and int(timestamp) < 18):
    print("Good Afternoon")
elif(int(timestamp) > 18):
    print("Good Evening")
else:
    print("Good Night")

print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime