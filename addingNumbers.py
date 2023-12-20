evenNumbers = int(input("give me a number to work with: (range 1 till 1000)\n"))

even = 0

for number in range(1, evenNumbers + 1):
    if number % 2 == 0:
        even += number

print(f"The total of all even numbers in the range given = {even}")
