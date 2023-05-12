"""MQ Yes/No
Simplifies the input by converting it to lower case. Also, accepts y or n as
abbreviations. Print result of user choice as well as input - for testing
"""

# Ask the user if they have solved quiz before
show_instructions = input("Have you solved the quiz this game before? :").lower

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display instructions")