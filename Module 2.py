name = input('insert your name:')
print (f'Hello,{name}!')

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius ** 2

print(f"The area of the circle is {area}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(f"perimeter: {perimeter}")
print(f"area: {area}")

first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))
third = int(input("Enter third integer: "))

total = first + second + third
product = first * second * third
average = total / 3

print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average}")

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talents = float(input("Enter talents:"))
pounds = float(input("enter pounds:"))
lots = float(input("Enter lots: "))


grams_per_lot =13.3
lots_per_pound =32
pounds_per_talent =20

total_lots = (
    talents * pounds_per_talent * lots_per_pound
    + pounds * lots_per_pound
    + lots
)

total_grams = total_lots * grams_per_lot

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

import random
digit3 = [random.randint(0, 9) for _ in range(3)]

digit4 = [random.randint(1, 6) for _ in range(4)]

print("3-digit code:", digit3)
print("4-digit code:", digit4)