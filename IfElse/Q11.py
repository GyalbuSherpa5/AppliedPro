# 11. The Date Is Correct or Not
from datetime import datetime

test_str = input("Enter the date.")

print("The original string is : " + str(test_str))

f = "%d-%m-%Y"

res = True

try:
    res = bool(datetime.strptime(test_str, f))
except ValueError:
    res = False

print("Does date match format? : " + str(res))
