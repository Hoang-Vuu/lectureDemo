#1
import random
def roll_dice():
    dice=random.randint(1,6)
    return dice
while True:
    if roll_dice()==6:
        print("The result is 6")
        break
    if roll_dice()!=6:
        print(f"The result is {roll_dice()}",)

#2
import random
sides = int(input("Enter the number of sides: "))
def dice_sides():
    dice=random.randint(1,sides)
    return dice
def main():
    roll=0
    while roll!=sides:
        print(f"The result is {dice_sides()}")
        roll+=1
        if roll==sides:
            print(f"The result is {sides}")
            break
main()

#3
def change_value():
    gallons = int(input("Enter the number of gallons: "))
    liters= gallons*3,785411784
    if gallons>=0:
        print(f"{gallons} gallons = {liters} liters")
    if gallons<0:
        print("Invalid input")
        return false


def main():
    while True:
        if not change_value():
            break

main()


#4
def integers():
    num= input("Enter the number of integers: ")
    nums =[]
    while num != "":
        nums.append(num)
        num= int(input("Enter the number of integers: "))
        if num =="":
            print(nums)
            print(sum(nums))
            break
integers()
