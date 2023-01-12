print("Welcome to Pizza Order Price Calculator")
print("=========================================")

size = input('Which side pizza you want to order?\n Small "S", Medium "M", Large "L": ')
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

print("=========================================")

bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill += 4
    elif add_pepperoni == "Y" and extra_cheese == "N":
        bill += 3
    elif add_pepperoni =="N" and extra_cheese == "Y":
        bill += 1
    
    print(f"Your final bill is ${bill}.")


elif size == "M":
    bill = 20
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill += 4
    elif add_pepperoni == "Y" and extra_cheese == "N":
        bill += 3
    elif add_pepperoni =="N" and extra_cheese == "Y":
        bill += 1
    
    print(f"Your final bill is: ${bill}.")

elif size == "L":
    bill = 25
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill += 4
    elif add_pepperoni == "Y" and extra_cheese == "N":
        bill += 3
    elif add_pepperoni =="N" and extra_cheese == "Y":
        bill += 1
    
    print(f"Your final bill is ${bill}.")

print("=========================================")
