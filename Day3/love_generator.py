print("Welcome to Love Calculator")
print("=============================")

name1 = input("Type your name: ").lower()
name2 = input("Type your partner name: ").lower()

combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l+o+v+e

total = int(str(true) + str(love))

print("=============================")

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}.")

print("=============================")
