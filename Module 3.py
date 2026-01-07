length = float(input("Enter the length of the zander (cm): "))

size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print(f"Release the fish back into the lake.")
    print(f"The fish was {difference:.1f} cm below the size limit.")
else:
    print("The zander meets the size limit.")

cabin_class = input("Enter cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin > 155:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin > 167:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

else:
    print("Invalid gender.")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not a leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
