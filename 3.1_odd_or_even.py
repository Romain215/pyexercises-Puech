"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A whole number N typed by the user in the terminal era.
# 2. Process: The program checks that N is valid. If it is, it goes through every
#    number from 1 to N and checks whether each one is odd or even.
# 3. Out:One line per number, saying "is odd" or "is even". If N is not valid,
#    a single error message instead appeared.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0: error message, because there is no number between 1 and 0 to check.
#    - Negative number (ex :-4): error message, because the list from 1 to -4
#      makes no sense.
#    - Very large number (ex : 5000): refused above 100, to avoid printing
#      thousands of useless lines. The message tells the user the maximum (100).


# Your code below
MAXIMUM = 100

n = int(input("Enter a number: "))

if n == 0:
    print("Zero is not valid: please enter a number greater than 0.")
elif n < 0:
    print("A negative number is not valid: please enter a number greater than 0.")
elif n > MAXIMUM:
    print("Too large: the maximum is", MAXIMUM)
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")