#Create function to generate data randomly with python standard library
import random

def generate_random_data(num_items, min_value, max_value):
    data = []
    for i in range(num_items):
        data.append(random.randint(min_value, max_value))
    return data


print(generate_random_data(22, -100, 100))