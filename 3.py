#1
length = float(input("Enter length of zander in cm:"))
if length <=42:
    print("You should release the fish back into the lake and the below size limit was 42 cm")
else:
    print("Available")


#2
cabin = input("Enter cabin:")
if cabin == "LUX":
    print("Upper cabin with a balcony")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck")
elif cabin == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")


#3
gender= input("Enter your gender:")
if gender == "male":
    value = float(input("Enter your hemoglobin value:"))
if gender == "female":
    value1=float(input("Enter your hemoglobin value:"))

if (gender == "male" and 134 <= value <= 167):
    print("normal")
elif  (gender == "male" and value > 167):
    print("high")
elif  (gender == "male" and value < 134):
    print("low")

if (gender=="female" and 117<= value1 <= 155):
    print("normal")
elif (gender=="female" and value > 155):
    print("high")
elif (gender=="female" and value < 117):
    print("low")


#4
year= int(input("Enter year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("It is a leap year")
else:
    print("It is a regular year")