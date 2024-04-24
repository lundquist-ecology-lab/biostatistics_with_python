import random

# Define the categorical variables
colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Brown"]
fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple", "Strawberry", "Kiwi", "Blueberry", "Watermelon", "Grape"]
animals = ["Dog", "Cat", "Lion", "Elephant", "Giraffe", "Zebra", "Monkey", "Tiger", "Bear", "Kangaroo"]

def generate_examples(categorical_var):
    examples = []
    categories = {
        "colors": colors,
        "fruits": fruits,
        "animals": animals
    }

    selected_categories = categories.get(categorical_var, [])

    if selected_categories:
        for i in range(10):
            example = random.choice(selected_categories)
            examples.append(example)
    else:
        print(f"Invalid categorical variable: {categorical_var}")

    return examples

def check_categorical_answers(user_answers, examples, categorical_var, num_categories):
    correct_count = 0
    categories = {
        "colors": colors,
        "fruits": fruits,
        "animals": animals
    }

    selected_categories = categories.get(categorical_var, [])
    num_actual_categories = len(set(selected_categories))

    if num_categories == num_actual_categories:
        print(f"Correct! The categorical variable '{categorical_var}' has {num_actual_categories} levels.")
    else:
        print(f"Incorrect. The categorical variable '{categorical_var}' has {num_actual_categories} levels, not {num_categories}.")

    for i, (example, user_answer) in enumerate(zip(examples, user_answers)):
        correct_answer = str(selected_categories.index(example) + 1)
        if user_answer == correct_answer:
            print(f"Correct! '{example}' belongs to category {correct_answer}.")
            correct_count += 1
        else:
            print(f"Incorrect. '{example}' belongs to category {correct_answer}, not {user_answer}.")

    print(f"\nYou got {correct_count} out of {len(examples)} correct.")