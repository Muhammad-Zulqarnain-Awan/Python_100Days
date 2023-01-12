print("Welcome to BMI calculator")
print("=========================================")

weight = int(input("What is your weight in kg? "))
height = float(input("What is your height? "))

print("=========================================")

bmi = int(weight / (height**2))

if bmi  < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >=18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >=25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
print("=========================================")
