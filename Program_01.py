# Program 1: Number Sorter
# Create a program that ask 4 numbers.
# Print the 4 numbers from highest to lowest using only if-else statement.

# Get 4 numbers.
def get_4_numbers():
    no_01 = int(input("Enter a number:"))
    no_02 = int(input("Enter a number:"))
    no_03 = int(input("Enter a number:"))
    no_04 = int(input("Enter a number:"))
    return no_01, no_02, no_03, no_04

# Arrange the 4 numbers from highest to lowest.


def high_low(no_01, no_02, no_03, no_04):
    highest = max(no_01, no_02, no_03, no_04)
    lowest = min(no_01, no_02, no_03, no_04)
    if highest == no_01:
        if lowest == no_04:
            if no_02 > no_03:
                print(f"The sequence is {no_01},{no_02},{no_03},{no_04}.")
            else:
                if no_02 < no_03:
                    print(f"The sequence is {no_01},{no_03},{no_02},{no_04}.")
        elif lowest == no_02:
            if no_03 > no_04:
                print(f"The sequence is {no_01},{no_03},{no_04},{no_02}.")
            else:
                if no_04 > no_03:
                    print(f"The sequence is {no_01},{no_04},{no_03},{no_02}.")
        else:
            if lowest == no_03:
                if no_04 > no_02:
                    print(f"The sequence is {no_01},{no_04},{no_02},{no_03}.")
                else:
                    if no_04 < no_02:
                        print(
                            f"The sequence is {no_01},{no_02},{no_04},{no_03}.")
    elif highest == no_02:
        if lowest == no_04:
            if no_03 > no_01:
                print(f"The sequence is {no_02},{no_03},{no_01},{no_04}.")
            else:
                if no_03 < no_01:
                    print(f"The sequence is {no_02},{no_01},{no_03},{no_04}.")
        elif lowest == no_01:
            if no_03 > no_04:
                print(f"The sequence is {no_02},{no_03},{no_04},{no_01}.")
            else:
                if no_03 < no_02:
                    print(f"The sequence is {no_02},{no_04},{no_03},{no_01}.")
        else:
            if lowest == no_03:
                if no_04 > no_01:
                    print(f"The sequence is {no_02},{no_04},{no_01},{no_03}.")
                else:
                    if no_04 < no_01:
                        print(
                            f"The sequence is {no_02},{no_01},{no_04},{no_03}.")

    elif highest == no_03:
        if lowest == no_01:
            if no_02 > no_04:
                print(f"The sequence is {no_03},{no_02},{no_04},{no_01}.")
            else:
                if no_02 < no_04:
                    print(f"The sequence is {no_03},{no_04},{no_02},{no_01}.")
        elif lowest == no_02:
            if no_01 > no_04:
                print(f"The sequence is {no_03},{no_01},{no_04},{no_02}.")
            else:
                if no_01 < no_04:
                    print(f"The sequence is {no_03},{no_04},{no_01},{no_02}.")
        else:
            if lowest == no_04:
                if no_01 > no_02:
                    print(f"The sequence is {no_03},{no_01},{no_02},{no_04}.")
                else:
                    if no_01 < no_02:
                        print(
                            f"The sequence is {no_03},{no_02},{no_01},{no_04}.")

    elif highest == no_04:
        if lowest == no_03:
            if no_02 > no_01:
                print(f"The sequence is {no_04},{no_02},{no_01},{no_03}.")
            else:
                if no_02 < no_01:
                    print(f"The sequence is {no_04},{no_01},{no_02},{no_03}.")
        elif lowest == no_02:
            if no_01 > no_03:
                print(f"The sequence is {no_04},{no_01},{no_03},{no_02}.")
            else:
                if no_01 < no_03:
                    print(f"The sequence is {no_04},{no_03},{no_01},{no_02}.")
        else:
            if lowest == no_01:
                if no_02 > no_03:
                    print(f"The sequence is {no_04},{no_02},{no_03},{no_01}.")
                else:
                    if no_02 < no_03:
                        print(
                            f"The sequence is {no_04},{no_03},{no_02},{no_01}.")


n1, n2, n3, n4 = get_4_numbers()
high_low(n1, n2, n3, n4)
