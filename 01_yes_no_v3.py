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


