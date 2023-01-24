def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime = False
    
    if is_prime and number!=1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

number = int(input("Enter the number: "))
prime_checker(number=number)