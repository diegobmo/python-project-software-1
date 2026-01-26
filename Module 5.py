import random

n = int(input("How many dice to roll? "))
total = 0

for _ in range(n):
    total += random.randint(1, 6)

print("Sum is", total)

numbers = []

while True:
    value = input("Enter a number (empty to quit): ")
    if value == "":
        break
    numbers.append(float(value))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)

n = int(input("Enter an integer: "))

if n < 2:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

cities = []

for _ in range(5):
    city = input("Enter city name: ")
    cities.append(city)

for city in cities:
    print(city)