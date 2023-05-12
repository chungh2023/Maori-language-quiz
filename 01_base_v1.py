# Ask the user if they have solved quiz before
show_instructions = input("Have you solved the quiz this game before? :")

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display instructions")