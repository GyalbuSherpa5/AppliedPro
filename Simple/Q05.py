first = input("Enter your first name ")
middle = input("Enter your middle name if you have ")
last = input("Enter your last name ")

if (len(middle) < 1):
    print(first[0] + "." + last)
else:
    print(first[0] + "." + middle[0] + "." + last)
