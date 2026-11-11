"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of monthly budgets built in exercise 4.0.
# 2. Process: the list is reordered in four different ways, always working on
#    copies so that the original is never changed.
# 3. Out: the four reordered lists, then the original list to prove it is intact.
# 4. My four orders, and which ones modify the original:
#     - Ascending, with sorted(): returns a new list, original untouched.
#    - Descending, with sorted(reverse=True): returns a new list, original untouched.
#    - Backwards, with [::-1]: returns a new list, original untouched.
#    - Alphabetical, with .sort(key=str): .sort() modifies a list in place, so I
#      used it on a copy. Used directly on the original, it would have changed it.


# Your code below
monthly_budgets = [1200, 850, 400, 2300, 650, 1500, 300, 950]

# The whole list
print("The whole list is: ", monthly_budgets)

# One item of my choice (the first one)
print("The first budget is: ", monthly_budgets[0])

# The sorted list
sorted_budgets = sorted(monthly_budgets)
print("The sorted list is: ", sorted_budgets)

# Something computed from the list
total = sum(monthly_budgets)
average = total / len(monthly_budgets)
print("The total budget is: ", total)
print("The average budget is: ", average)