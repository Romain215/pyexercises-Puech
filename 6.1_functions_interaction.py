"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of grades (numbers between 0 and 20)
# 2. Process, function by function:
#    - is_at_least(grade, threshold): tells if a grade is greater than or equal to the threshold
#    - keep_passing_grades(grades): returns the list of grades >= 10
#    - count(items): returns the number of items in a list
#    - number_of_passing_grades(grades): uses the three others to count the grades >= 10
# 3. Out: an integer (how many grades are >= 10)
# 4. The question my fourth function answers:
#    "How many students got at least 10/20?"
#    Splitting it into three makes it easier to check: if the result is wrong,
#    I can test each small function on its own and find which one is wrong,
#    instead of searching for the bug in one big block of code.


# Your code below
number = -4
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

number = 5
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

number = 9
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

def check(number):
    if number > 0:
        print("The number is positive")
    else:
        print("The number is negative")

num = int(input("Enter a number:"))
check(num)



def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

def is_zero(num):
    return num == 0

def is_even(num):
    return num % 2 == 0

def detailed_message(num):
    if is_zero(num):
        return "The number is zero."
    elif is_positive(num):
        return "The number is positive."
    elif is_negative(num):
        return "The number is negative."
    elif is_even(num):
        return "The number is even."
    else:
        return "The number is odd."

number = 0
print(detailed_message(number))