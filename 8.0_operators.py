"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two values I chose: the strings "Apple" and "apple"
#    (the same word, only the capital letter is different)
#
# 2. What happens:
#    - The program compares the two values with every comparison operator:
#      ==, !=, <, >, <=, >=
#    - Then it combines some of these results with the logical operators
#      and, or, not
#    - Each operation and its result (True or False) is stored in a list of tuples
#
# 3. Out: a readable table in the terminal, one line per operation,
#    with the operation on the left and the result (True / False) on the right.
#
# 4. Which two values did I pick, and which result surprised me?
#    I picked "Apple" and "apple".
#    The surprise: "Apple" < "apple" is True. Python compares strings letter by
#    letter using their Unicode code: "A" is 65 and "a" is 97, so every
#    uppercase letter comes BEFORE every lowercase letter.
#    Also, "Apple" == "apple" is False: for Python, they are two different words.
#    To compare them without caring about capitals, I must use .lower() first.
#
# Check: I predicted each result before running. I got 6 out of 11 right.


# Your code below

value_a = "Apple"
value_b = "apple"

# Every comparison between the two values
comparisons = [
    ("a == b", value_a == value_b),
    ("a != b", value_a != value_b),
    ("a < b", value_a < value_b),
    ("a > b", value_a > value_b),
    ("a <= b", value_a <= value_b),
    ("a >= b", value_a >= value_b),
]

# Logical combinations of those results
equal = value_a == value_b
smaller = value_a < value_b
combinations = [
    ("(a == b) and (a < b)", equal and smaller),
    ("(a == b) or (a < b)", equal or smaller),
    ("not (a == b)", not equal),
    ("not (a < b)", not smaller),
    ("a.lower() == b.lower()", value_a.lower() == value_b.lower()),
]

# Display the table
print("a =", repr(value_a), "| b =", repr(value_b))
print()
print(f"{'Operation':<25}{'Result'}")
print("-" * 32)
for operation, result in comparisons + combinations:
    print(f"{operation:<25}{result}")

