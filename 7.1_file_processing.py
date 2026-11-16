"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are empty lines (lines 3 and 9).
# - Some lines start with extra spaces ("  alan TURING", "  linus torvalds").
# - The capital letters are inconsistent: some names are all lowercase ("grace hopper"),
#   some are all uppercase ("GUIDO"), some are mixed ("ada LOVELACE").
# - One name has three words: "GUIDO van rossum". The last name is "van Rossum",
#   and "van" is a particle that should stay lowercase.
# - The names are not sorted.

# 1. In: the file names.txt (10 lines, one name per line, with the problems above)
#
# 2. Process, problem by problem:
#    - Empty lines: remove_empty_lines() keeps only the lines that contain text.
#    - Extra spaces: clean_spaces() removes spaces at the start and end,
#      and keeps only one space between words.
#    - Capital letters: fix_capitals() puts a capital at the start of each word
#      and lowercase for the rest, except particles like "van" that stay lowercase.
#    - Not sorted: names.sort(key=last_name_key) sorts the list by last name.
#    - The original file is only opened in read mode ("r"), so it is never modified.
#
# 3. Out: a new file names_sorted.txt with 8 clean names, one per line,
#    sorted by last name. The format is "First Last", for example "Ada Lovelace".
#
# 4. How I decide which word is the last name:
#    The first word is the first name and the last word is the last name.
#    For "Guido van Rossum", the full last name is "van Rossum", but I sort with
#    the last word only, "Rossum", like in Dutch, where the particle "van" is ignored
#    for sorting. So Guido van Rossum goes under R, between Lovelace and Torvalds.
#
# Check:
#    names.txt has 10 lines, names_sorted.txt has 8 lines.
#    The difference is 2, because the 2 empty lines were removed.
#    First name of the sorted list: Margaret Hamilton (H). Last: Alan Turing (T).


# Your code below

INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_sorted.txt"
PARTICLES = ["van", "von", "de", "da", "du", "le"]


def read_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()


def remove_empty_lines(lines):
    result = []
    for line in lines:
        if line.strip() != "":
            result.append(line)
    return result


def clean_spaces(line):
    return " ".join(line.split())


def fix_capitals(name):
    words = []
    for word in name.split():
        if word.lower() in PARTICLES:
            words.append(word.lower())
        else:
            words.append(word.capitalize())
    return " ".join(words)


def last_name_key(name):
    return name.split()[-1].lower()


def write_lines(file_name, names):
    with open(file_name, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


lines = read_lines(INPUT_FILE)
lines = remove_empty_lines(lines)
names = []
for line in lines:
    names.append(fix_capitals(clean_spaces(line)))
names.sort(key=last_name_key)
write_lines(OUTPUT_FILE, names)

print("Lines in", INPUT_FILE, ":", len(read_lines(INPUT_FILE)))
print("Lines in", OUTPUT_FILE, ":", len(names))