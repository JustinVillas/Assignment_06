# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0-99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# Put
from random import randint
from operator import add


def add_skill_test():
    items = 0
    score = 0
    for items in range(10):
        no_01 = randint(0, 99)
        no_02 = randint(0, 99)
        # Computer will add the two random numbers.
        ans_computer = add(no_01, no_02)
        # Ask the sum of two random numbers.
        ans_user = int(input(f"{no_01} + {no_02} = "))
        # Compare if user have the same answer with the computer
        if ans_computer == ans_user:
            print(f"You are correct! ")
            score = score + 1
            items = items + 1
        # If user doesn't have the same answer. User is wrong
        else:
            if not ans_computer == ans_user:
                print(
                    f"You need to practice more. Correct answer is {ans_computer}.")
                items = items + 1
        # The total items is 10.
        if items == 10:
            # Display the result summary of the 10 operations (ex 9/10)
            print(f"{score}/{items}")
        else:
            if score == 0:
                print(f"{score}/{items}")


add_skill_test()
