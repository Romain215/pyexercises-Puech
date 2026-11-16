"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: text typed by the user (input() always returns a string).
# 2. Process: the text is converted to a number with float(), then 100 is
#    divided by that number.
# 3. Out: the result of the division, or a clear error message. The program
#    asks again instead of crashing.
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: the conversion fails because the text is not a number
#      ("abc"). This is an INPUT error.
#    - ZeroDivisionError: the text is a valid number, but it is 0 and we
#      cannot divide by 0. This is a limit of the CALCULATION (like a
#      campaign with zero conversions).
#    They do NOT deserve the same message: in the first case the user must
#    type digits, in the second they must choose a number other than 0.
#    A single message would not tell them what to fix.
#
# Number of attempts allowed: 3, then the program stops cleanly.
#
# Why catch each failure separately instead of "except Exception":
#    - each problem gets its own, helpful message;
#    - "except Exception" would also catch our own bugs (for example a typo
#      in a variable name, NameError). The program would say "invalid input"
#      when the mistake is in the code, and we would never see it;
#    - a bare "except:" would even catch Ctrl+C, so the user could no longer
#      stop the program.
#
# The 4 test runs (CHECK IT YOURSELF):
#    - "4"   -> prints "100 / 4.0 = 25.0" and the program ends.
#    - "0"   -> prints the division-by-zero message and asks again.
#    - "abc" -> prints the "not a number" message and asks again.
#    - ""    -> (empty line) prints "You did not type anything" and asks
#               again. Without the special check, float("") would raise the
#               same ValueError as "abc"; we detect it first to give a
#               clearer message.
#    After 3 failed attempts, the program prints a message and stops
#    without crashing.


# Your code below

MAX_ATTEMPTS = 3
VALUE = 100

for attempt in range(1, MAX_ATTEMPTS + 1):
    user_input = input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter a number: ")

    # Empty line: handled separately to give a more precise message.
    if user_input.strip() == "":
        print("You did not type anything. Please enter a number.")
        continue

    try:
        number = float(user_input)
        result = VALUE / number
    except ValueError:
        print(f"'{user_input}' is not a number. Please type digits (e.g. 4 or 2.5).")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please choose a number other than 0.")
    else:
        print(f"{VALUE} / {number} = {result}")
        break
else:
    print(f"{MAX_ATTEMPTS} failed attempts. The program is stopping.")
