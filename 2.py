import random

#1
name = input("Enter your name:")
print("Hello", name)

#2
rds = float(input("Enter RDS:"))
area= 3.14 * (rds ** 2)
print(f"You RDS is,{rds}, and your area is,{area}")

#3
length = float(input("Enter length:"))
width = float(input("Enter width:"))
perimeter =  length *2 + width *2
area1 = length * width
print(f"The perimeter is {perimeter}, and the area is {area1}")

#4
num1 = float(input("enter first number:"))
num2 =float(input("enter second number:"))
num3 = float(input("enter third number:"))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print(f"The sum is {sum}, and the product is {product}, and the average is {average}")

#5
talents= float(input("Enter number of talents:"))
pounds= float(input("Enter number of pounds:"))
lots= float(input("Enter number of lots:"))
grams= float(talents*20*32*13.3 + pounds*32*13.3 + lots * 13.3)
kilograms= int(grams/1000)
grams_left= grams- kilograms *1000
print(f"The weight in modern unit is {kilograms} kg, and {grams_left:.2f} grams")

#6
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
print(f"{num1}{num2}{num3}")

num4 = random.randint(1, 6)
num5 = random.randint(1, 6)
num6 = random.randint(1, 6)
num7 = random.randint(1, 6)
print(f"{num4}{num5}{num6}{num7}")

