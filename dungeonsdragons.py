print("""

___  _  _ _  _ ____ ____ ____ _  _ ____       ___  ____ ____ ____ ____ _  _ ____ 
|  \ |  | |\ | | __ |___ |  | |\ | [__        |  \ |__/ |__| | __ |  | |\ | [__  
|__/ |__| | \| |__] |___ |__| | \| ___]       |__/ |  \ |  | |__] |__| | \| ___] 
                                                                            
""")
print("Welcome to Dungeons & Dragons\n")

player_name = input("What is your name, adventurer: ")

health = 100
damage = 20

print("Welcome, " + player_name + " you have " + str(health) + " health and can do damage " + str(damage))
print("You came across a dragon!! What will you do??\n")
print("1. Fight!")
print("2. Run!")

choice = int(input("Enter either 1 or 2: "))
if choice == 1:
    print("Attack the dragon now!!!...")
    print("Dont let it go!!...")
    health -= 10
    print("Awww.... i get fire by the dragon. My current health now is " + str(health))
    print("I will kill you dragon!!!....")
    print("You really piss me off")


elif choice == 2:
    print("Run away from the dragon!...")
    print("Dont let it destroy you!...")
    print("We will figth the dragon another day...")
    print("Oh NOOOO!!.. The dragon is above us...")
    print("Go hide!!!!")

    health1 = 100
    health1 -= 20

    print("Awww. the dragon trow rock at me!...")
    print("My current health now is: " + str(health1))

else:
    print("Invalid Choise!...")
    print("The dragon has eat you alive...")










