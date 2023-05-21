# Functions
def yes_no(question_text):
    while True:

        # Ask the user if they want to take this quiz
        answer = input(question_text).lower()

        # If they say yes, output 'Program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'End the quiz'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer


# Main routine
show_instructions = yes_no("If you want to take this quiz? ")
print(f"You entered '{show_instructions}'")
print()

def get_name():
    name_local = input("what is your name: ")
    return name_local


def get_age():
    age_local = input("How old are you: ")
    return age_local


# Main routine
name = get_name()  # 1st function
age = get_age() # 2nd function
print(f"\nHi {name}. At {age} years old, you might find this a bit easy.\n"
      "\nAnyway, this is a test about number of Māori.\n"
      "You will need to enter the correct number abbreviation which question "
      "e.g. tahi for 1 \n")

import random

numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["whā", "4"], ["rima", "5"],
        ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

random.shuffle(numbers)

for i in numbers:
    answer = input(f"Enter the correct number abbreviation which questions to {i[0]}: ")
    if answer == i[1]:
        print("##### CORRECT! ######\n")
    else:
        print("XXXXX INCORRECT XXXXX\n")
