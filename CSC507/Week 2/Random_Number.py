import time

# Record the start time
start_time = time.time()
print("Start Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))

#!/usr/bin/env python3
import random

# Generate a list of 10000000 random numbers between 1 and 100000
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Write the numbers to a text file
with open("file2.txt", "w") as file:
    for number in random_numbers:
        file.write(f"{number}\n")

print("Random numbers have been written to 'file2.txt'.")

# Record the end time
end_time = time.time()
print("End Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))

# Calculate and display the time difference
elapsed_time = end_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Elapsed Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")