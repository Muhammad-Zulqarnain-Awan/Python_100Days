print("Welcome to Tip Calculator")

no_peoples=int(input("Enter the number of peoples: "))
bill_amount=float(input("Enter the bill amount: "))

total_amount=round((bill_amount/no_peoples)*1.12,2)

print(f"Your total bill after adding 12% tip is ${total_amount}.")
print("Thank you")
