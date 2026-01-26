number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

    while True:
        inches = float(input("Enter inches (negative value to quit): "))

        if inches < 0:
            break

        centimeters = inches * 2.54
        print(f"{centimeters:.2f} cm")

    smallest = None
    largest = None

    while True:
        user_input = input("Enter a number (empty to quit): ")

        if user_input == "":
            break

        number = float(user_input)

        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number

    if smallest is not None:
        print("Smallest number:", smallest)
        print("Largest number:", largest)
    else:
        print("No numbers entered.")

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Wrong credentials")
        attempts += 1

if attempts == 5:
    print("Access denied")

import random

points = int(input("How many random points to generate? "))

inside_circle = 0
for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        inside_circle += 1

pi_approx = 4 * inside_circle / points

print("Approximation of pi:", pi_approx)