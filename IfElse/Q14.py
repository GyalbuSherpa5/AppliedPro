#14. Find the maximum between the three numbers.
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

maximum = 0

if a > b and a > c:
    maximum = a
elif b > c:
    maximum = b
else:
    maximum = c

print(maximum, "is the maximum between three numbers.")