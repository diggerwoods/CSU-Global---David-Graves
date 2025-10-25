import random

# Generate a list of 1000 random numbers between 1 and 100000
random_numbers = [random.randint(1, 100000) for _ in range(1000)]

# Write the numbers to a text file
with open("file2.txt", "w") as file:
    for number in random_numbers:
        file.write(f"{number}\n")

print("Random numbers have been written to 'file2.txt'.")