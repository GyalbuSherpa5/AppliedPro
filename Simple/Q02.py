# 2. Area and Circumference of a Circle
import math

radius = int(input("Enter radius "))

area = round(math.pi * (radius ^ 2), 2)
print("Area of circle is ", area)
cir = round(2 * (math.pi * radius), 2)
print("Area of circumference of circle is ", cir)
