name = input("Please enter your name: ")
mark = int(input("Please enter your mark: "))

if mark >= 80:
    gred = ("you are brilliant")
    print("Hi " + name +", your mark " + str(mark) + ", " + str(gred))

    

elif mark <= 79:
    gred1 = ("you did okay. Better luck next time")
    print("Hi " + name + ", your mark " + str(mark) + ", " + str(gred1))

    