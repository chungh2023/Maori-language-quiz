show_instructions = ""
while show_instructions != "x":


    # Ask the user if they want to take this quiz
    show_instructions = input("If you want to take this quiz? :").lower()

    # If they say yes, output 'Program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    # If they say no, output 'End the quiz'
    elif show_instructions == "no" or show_instructions == "n":
        print("End the quiz")



