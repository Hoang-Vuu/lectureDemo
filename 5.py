#1
import random
result =[]
rolls = int(input("How many times do you want to roll? "))
for n in range(rolls):
    random.randint(1,6)
    result.append(random.randint(1,6))
print("The result is",sum(result))

#2
nums=[]
while True:
    num= input("Enter a number: ")
    nums.append(num)
    if num == "":
        break
nums.remove("")
nums.sort()
print(nums)

#3
num = int(input("Enter a number: "))
for n in range(2,num-1):
    if num % n == 0:
        print(f"{num} is not the prime number")
        break
    else:
        print(f"{num} is a prime number")
        break

#4
cities =[]
city = input("Enter city:")
while city !="":
        cities.append(city)
        city= input("Enter city:")
        if city == "":
            print(cities)
            break
for n in cities:
    print(n)
