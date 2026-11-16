"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: four permissions on an ad campaign, each one stored as one bit:
#    VIEW = 0001 (1), EDIT = 0010 (2), PUBLISH = 0100 (4), BUDGET = 1000 (8)
#
# 2. What happens:
#    - Step 1: I give an intern two permissions, VIEW and EDIT, combined with | (OR)
#    - Step 2: I test whether the intern can publish, with & (AND)
#    - Step 3: I add PUBLISH with |
#    - Step 4: I remove EDIT with & ~ (AND NOT)
#    - At each step, the value is shown in decimal and in binary
#
# 3. Out: a table in the terminal with each step, the value in decimal and its 4 bits,
#    plus True / False when I test a permission.
#
# 4. What are my permissions about?
#    Who can do what on an ad campaign in a marketing team:
#    - VIEW: see the campaign and its results (clicks, sales)
#    - EDIT: change the texts, images and targeting
#    - PUBLISH: put the campaign online
#    - BUDGET: change the money spent on the campaign
#    Example: an intern can view and edit, but only the manager can publish
#    and change the budget.
#
# Check: I read the bits myself at each step.
#    0011 = VIEW + EDIT, 0111 = VIEW + EDIT + PUBLISH, 0101 = VIEW + PUBLISH


# Your code below

# Each permission is one bit
VIEW = 0b0001     # 1: can see the campaign and its results
EDIT = 0b0010     # 2: can change texts, images and targeting
PUBLISH = 0b0100  # 4: can put the campaign online
BUDGET = 0b1000   # 8: can change the money spent on the campaign


# Show one step: its name, the value in decimal and in binary (4 bits)
def show(step, permissions):
    print(f"{step:<38}{permissions:>3}  {permissions:04b}")


# Return True if the permission is in the set
def has_permission(permissions, permission):
    return permissions & permission != 0


print(f"{'Step':<38}{'Dec':>3}  Bits")
print("-" * 48)

# Step 1: combine two permissions with | (OR)
intern = VIEW | EDIT
show("1. Intern = VIEW | EDIT", intern)

# Step 2: test whether a third one is present with & (AND)
print("2. Can the intern publish?", has_permission(intern, PUBLISH))

# Step 3: add PUBLISH with |
intern = intern | PUBLISH
show("3. Add PUBLISH: intern | PUBLISH", intern)
print("   Can the intern publish now?", has_permission(intern, PUBLISH))

# Step 4: remove EDIT with & ~ (AND NOT)
intern = intern & ~EDIT
show("4. Remove EDIT: intern & ~EDIT", intern)
print("   Can the intern still edit?", has_permission(intern, EDIT))
