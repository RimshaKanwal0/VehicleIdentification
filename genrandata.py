# -*- coding: utf-8 -*-
"""GenRanData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eH5vRV3PEXNwd33cLwxcjYcZ8Zbubhqx
"""

import random
import csv

class Vehicle:
    def __init__(self, weight, height, color):
        self.weight = weight
        self.height = height
        self.color = color
        self.no_of_wheels = self.determine_wheels()

    def determine_wheels(self):
        if self.weight <= 1200:
            return 2
        elif self.weight > 1800:
            return 4
        else:
            return random.choice([2, 4])

def generate_random_data(num_entries):
    data = []
    for _ in range(num_entries):
        # Weight ranges from 800 to 2500
        weight = random.randint(800, 2500)
        # Height ranges from 50 to 180
        height = random.randint(50, 180)
        color = random.choice(['red', 'blue', 'green', 'yellow', 'black', 'white'])
        vehicle = Vehicle(weight, height, color)
        data.append([vehicle.weight, vehicle.height, vehicle.color, vehicle.no_of_wheels])
    return data

# Generate 5000 random data entries
random_data = generate_random_data(5000)

# Save the random data entries to a CSV file
with open('random_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['weight', 'height', 'color', 'no_of_wheels'])
    writer.writerows(random_data)

print("CSV file 'random_data.csv' with 5000 entries has been created.")