import random

# Define the lists at the module level
discrete_data = ["number of children in a family", "number of cars owned", "number of floors in a building", "number of books on a shelf", "number of students in a class", "number of siblings", "number of legs on an insect", "number of coins in a jar", "number of pets owned", "number of doors in a room"]
continuous_data = ["height of a person", "weight of an object", "temperature of a room", "time taken to run a marathon", "distance between two cities", "amount of rainfall", "speed of a car", "volume of a liquid", "area of a shape", "length of a rope"]

def generate_examples():
    examples = []
    remaining_discrete = discrete_data.copy()
    remaining_continuous = continuous_data.copy()

    for i in range(10):
        data_type = random.choice(["discrete", "continuous"])
        if data_type == "discrete":
            if remaining_discrete:
                example = random.choice(remaining_discrete)
                remaining_discrete.remove(example)
            else:
                # If no more discrete examples are available, choose from continuous data
                example = random.choice(remaining_continuous)
                remaining_continuous.remove(example)
        else:
            if remaining_continuous:
                example = random.choice(remaining_continuous)
                remaining_continuous.remove(example)
            else:
                # If no more continuous examples are available, choose from discrete data
                example = random.choice(remaining_discrete)
                remaining_discrete.remove(example)
        examples.append(example)

    return examples

def check_answers(user_answers):
    examples = generate_examples()
    correct_count = 0
    for i, (example, user_answer) in enumerate(zip(examples, user_answers)):
        data_type = "discrete" if example in discrete_data else "continuous"
        if user_answer.lower() == data_type:
            print(f"Correct! '{example}' is {data_type} data.")
            correct_count += 1
        else:
            print(f"Incorrect. '{example}' is {data_type} data, not {user_answer.lower()} data.")

    print(f"\nYou got {correct_count} out of {len(examples)} correct.")