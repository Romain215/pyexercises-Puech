"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of grades (numbers between 0 and 20)
# 2. Process: add up all the grades, then divide by the number of grades
# 3. Out: the average (a decimal number, a float)
# 4. My function name: average_grade. The name says what it computes,
#    no need to read the code to understand it.
#
#    Why return rather than print:
#    print shows the result on the screen, but the program can't use it anymore.
#    return sends the value back to the program: we can store it in a variable,
#    compare it, use it in another calculation, or display it later if we want.
#    A function that prints can only display, a function that returns
#    can be reused anywhere.


# Your code below
number_1 = 0
number_2 = 20

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

number_1 = 1
number_2 = 2

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

number_1 = 4
number_2 = 3

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)


def add_numbers(num1, num2):
    sum_result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum_result)
    return sum_result
    


sum = add_numbers(10, 20)

print(sum)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = add_numbers(num1, num2)
print("Sum:", result)