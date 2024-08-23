
'''
num1 = int(input("enter firt number:"))
num2 =int(input("enter second number:"))
sum = num1 + num2
print(sum)


name = input("Enter your name:")
school= input("Enter your school:")
print("You are",name, "and your school is",school)

print(f" Your name is, {name}, and your school name is :{school}")
floatvariable = 3.486858
print(f"Your name is,{name}, and your floatvariable is,{floatvariable}")

rds = float(input("Enter RDS:"))
area= 3.14 * (rds ** 2)
print(f"You RDS is,{rds}, and your area is,{area}")


intvariable = 3
floatvariable = 3.14
stringvariable = "Maybe"

print(intvariable)
print(floatvariable)
print(stringvariable)

#typecasting
intvariable = int(floatvariable)
print("here is the int version of float variable",intvariable)

shareofloan= 500.50/3
print(shareofloan)
print(int(shareofloan))



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

'''
import random
num1= random.randint(1,100)

