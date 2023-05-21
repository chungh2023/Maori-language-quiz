import random


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

numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["whā", "4"], ["rima", "5"],
        ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["iwa", "9"], ["tekau", "10"]]

random.shuffle(numbers)

for i in numbers:
    answer = input(f"Enter the number abbreviation which applies to {i[0]}: ")
    if answer == i[1]:
        print("##### CORRECT! ######\n")
    else:
        print("XXXXX INCORRECT! XXXXX\n")

