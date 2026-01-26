import random

def roll_dice():
    return random.randint(1, 6)

while True:
    result = roll_dice()
    print(result)
    if result == 6:
        break
def roll_dice(sides):
    return random.randint(1, sides)

max_value = int(input("Enter number of sides: "))

while True:
    result = roll_dice(max_value)
    print(result)
    if result == max_value:
        break
def gallons_to_litres(gallons):
    return gallons * 3.785

while True:
    g = float(input("Enter gallons: "))
    if g < 0:
        break
    print(gallons_to_litres(g), "litres")

def list_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [1, 2, 3, 4, 5]
print(list_sum(nums))

def remove_uneven(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

original = [1, 2, 3, 4, 5, 6]
filtered = remove_uneven(original)

print("Original:", original)
print("Even only:", filtered)