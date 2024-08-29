
'''

#1
first=3
while first<=1000:
    print(first)
    first+=3

#2
inches= float(input("Enter inches: "))
while inches >=0:
    cm=inches * 2.54
    print(f"{inches} inches is {cm} cm")
    inches-=1
    if inches<=0:
        break

'''
#3
num = int(input("Enter a number: "))
while True:
        if num == "":
            break
        largest = max(num)
        smallest = min(num)
        print(f"The largest number is {largest}")
        print(f"The smallest number is {smallest}")


'''
#4
import random
num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != num:
    if guess > num:
        print("High")
        guess= int(input("Again: "))
    elif guess < num:
        print("low")
        guess= int(input("Again: "))
else:
    guess == num
    print("Correct")


#5
fails = 0
while True:
    user = input("Enter your username:")
    password = input("Enter your password:")
    if user == "python" and password == "rules":
        print("welcome")
        break
    elif (user != "python" or password != "rules") and fails <= 5:
        fails += 1
        print(f"incorrect, you have {5 - fails} times left")
    else:
        print("access denied")
        break
'''





