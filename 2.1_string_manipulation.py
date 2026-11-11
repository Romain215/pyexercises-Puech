"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my phrase wrote by my owne
# 2. Process: we input to it 4 textual transformation
# 3. Out: 4 version of my phrase
# 4. My four transformations, and when each is useful: # 4. My 4 transformations, and when each is useful:
# strip(): removes spaces at both ends. It can be Useful to clean what a user typed in a form (" Romain " becomes "Romain").
# upper(): puts everything in capitals. Useful to display a warning or a title (for example "ATTENTION").
# title(): capital letter on each word. Useful to display a name nicely ("Romain Puech" becomes "ROMAIN PUECH").
# replace(" ", "-"): replaces spaces with dashes. Useful to create a web address ("je-suis-romain").


# Your code below
sentence = input("Enter a sentence: ")

print(sentence.strip())
print(sentence.upper())
print(sentence.title())
print(sentence.replace(" ", "-"))