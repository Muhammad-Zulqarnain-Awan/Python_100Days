import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)


if user_choice == comp_choice:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("It's a draw!")

elif user_choice >=3 or user_choice < 0:
  print("Invalid Number. Choose only 0, 1 or 2.")
else:
  if user_choice == 0 and comp_choice == 1:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("Computer Win!")

  elif user_choice == 0 and comp_choice == 2:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("You Win!")

  elif user_choice == 1 and comp_choice == 0:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("You Win!")

  elif user_choice == 1 and comp_choice == 2:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("Computer Win!")

  elif user_choice == 2 and comp_choice == 0:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("Computer Win!")

  elif user_choice == 2 and comp_choice == 1:
    print(game_img[user_choice])
    print(f"Computer Choose: {comp_choice}")
    print(game_img[comp_choice])
    print("You Win!")

  
