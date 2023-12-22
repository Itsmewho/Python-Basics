print("Hello welcome to prime checker!")
prime = int(input("What is the number you want to check?\n"))

def prime_checker(number=prime):
    is_prime = True
    for prime in range(2, number):
        if number%prime ==0:
            is_prime = False
    if is_prime:
        print(f"'{number}', This is a prime.")
    else:
        print(f"'{number}', This is Not a prime.")
prime_checker()