#Mohd Shafizan Bin Abdullah
#01140749957
#yodeh9999@gmail.com

name = input("What is your name?\n")
greeting = "Hello " + name
print(greeting)

weight = float(input("What is your weight? \n"))

height = float(input("What is your height?\n"))

bmi = weight / (height * height) 
print(name + " " + ", your BMI is " + str(bmi))

