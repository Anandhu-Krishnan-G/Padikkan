import  random
while True:
    print("y:roll the dice")
    print("n:exit")
    dice=input("Plz select the option[y/n]")
    if dice=="y":
        n=random.randint(1,6)
        print("Dice number is"+str(n))
        if n==1:
            print("~~~~~~~~~~~")
            print("|         |")
            print("|         |")
            print("|    O    |")
            print("|         |")
            print("|         |")
            print("~~~~~~~~~~~")
        elif n==2:
            print("~~~~~~~~~~~")
            print("|         |")
            print("|       O |")
            print("|         |")
            print("| O       |")
            print("|         |")
            print("~~~~~~~~~~~")
        elif n==3:
            print("~~~~~~~~~~~")
            print("|         |")
            print("|       O |")
            print("|    O    |")
            print("| O       |")
            print("|         |")
            print("~~~~~~~~~~~")
        elif n==4:
            print("~~~~~~~~~~~")
            print("|         |")
            print("| O     O |")
            print("|         |")
            print("| O     O |")
            print("|         |")
            print("~~~~~~~~~~~")
        elif n==5:
            print("~~~~~~~~~~~")
            print("|         |")
            print("| O     O |")
            print("|    O    |")
            print("| O     O |")
            print("|         |")
            print("~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~")
            print("|         |")
            print("| O     O |")
            print("| O     O |")
            print("| O     O |")
            print("|         |")
            print("~~~~~~~~~~~")
    elif dice=="n":
        break
    else:
        print("Ooppsss.....")
        print("Invalid selection")



