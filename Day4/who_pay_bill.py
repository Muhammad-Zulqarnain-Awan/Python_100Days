import random

name_string = input("Give me everybody's names, seperated by a comma: ")
names = name_string.split(",")

#without choice method
name = random.randint(0,len(names)-1)
print(f"{names[name]} is going to buy the meal today!")


#with choice method
name = random.choice(names)
print(f"{name} is going to buy the meal today!")
