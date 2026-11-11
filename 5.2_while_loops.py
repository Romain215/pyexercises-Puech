"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# # 1. In: the answers typed by the user, one per attempt.
# 2. Process: the program asks "Do you want to continue?" again and again.
#    Each answer is cleaned (extra spaces removed, lowercase) and stored.
#    The loop stops when the answer is "yes" or when the limit is reached.
# 3. Out: a summary with the number of attempts, the list of answers given,
#    and a final message saying whether the user confirmed or not.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the user answers "yes". "Yes", "YES" and " yes " all
#      count as yes, because I clean the answer first.
#    - Attempt limit: 3. Without a limit, a user who never types "yes" would
#      keep the program running for ever.
#    - When the limit is reached: the program stops and says no "yes" was given.
#    - Summary: attempts used, answers given, and the final result.


# Your code below
MAX_ATTEMPTS = 3

attempts = 0
answers = []
confirmed = False

while attempts < MAX_ATTEMPTS:
    answer = input("Do you want to continue? (yes/no): ")
    attempts = attempts + 1
    cleaned = answer.strip().lower()
    answers.append(cleaned)

    if cleaned == "yes":
        confirmed = True
        break

    print("Not the expected answer. Attempt", attempts, "of", MAX_ATTEMPTS)

print("Summary")
print("Attempts used:", attempts)
print("Answers given:", answers)

if confirmed:
    print("The user confirmed with yes.")
else:
    print("Limit reached without a yes: the program stops.")