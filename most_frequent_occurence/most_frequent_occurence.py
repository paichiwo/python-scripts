import random
from collections import defaultdict


# Number of draws
num_draws = 100

# Initialize a dictionary to track the occurrence of each number
number_counts = defaultdict(int)

for _ in range(num_draws):
    all_numbers = [number for number in range(1, 81)]  # draw from 1 to 80
    lotto = random.sample(all_numbers, 6)  # choose six unique numbers

    # Find the most frequent numbers
    for number in lotto:
        number_counts[number] += 1

most_frequent_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

# Print the most frequent numbers and their occurrence times
print("Draws:", num_draws)
print("Most frequent numbers:")
for number, count in most_frequent_numbers[:10]:  # number of frequency results
    print(f"Number {number}: {count} times")

