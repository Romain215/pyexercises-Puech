"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# # 1. In: the list of names built in exercise 4.0 (written in the code).
# 2. Process: the program goes through the list one item at a time and
#    counts the letters of each name.
# 3. Out: one line per name, with its position, the name and its length.
#    8 items in the list, so 8 lines.
# 4. What I compute for each item, and why it is worth showing:
#    the number of letters of each name. It shows which names are long
#    and which are short, which is useful for example to check that a name
#    fits in a form field or a printed label.

# Your code below
names = ["Romain", "Pierre", "Fabienne", "Béa", "Laurent", "Dadou", "Théo", "Lou"]

print("List of names and their lengths:", names)

print("First item of the list is: ", names[0])
print("Second item of the list is: ", names[1])
print("Third item of the list is: ", names[2])

i = 1, 2, 3, 4, 5

for i in range(1, 10):
    print("Item", i)   

for i in names:
    length = len(i)
    print("Name: ", i, "Length:" , length)