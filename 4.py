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


#3
largest = 0
smallest = 0

while True:
    num = input("Enter a number: ")
    if num =="":
        break
    if largest == 0 or num >= largest:
        largest = num
    if smallest == 0 or num <= smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)





#4
import random
num = random.randint(1,10)
guess = int(input("Guess a number:"))
tried = 1
while guess != num:
    if guess > num:
        print("Your guess is high")
        guess = int(input(f"You tried {tried} times, guess again:"))
    elif guess < num:
        print("Your guess is low")
        guess = int(input(f"You tried {tried} times, guess again:"))
    tried = tried + 1
else:
        print("Your guess is correct")


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


#6
import random
N = int(input("Enter the number of points: "))
n = 0
x = random.uniform(-1,1)
y = random.uniform(-1,1)
while n<=N:
    if x**2+y**2<=1:
        n+=1
pi=4*n/N
print(f"The value of pi is {pi}")