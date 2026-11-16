"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: the user types a book title and the number of pages read today
#    (the date is added automatically)
# 2. Process:
#    - the program asks for the title and the pages, and asks again if a value is not acceptable
#      (empty title, or pages that are not a positive whole number)
#    - if the file does not exist yet, it writes the header line first
#    - it adds the new entry at the end of the file (mode "a" = append),
#      so running it twice gives two entries instead of overwriting the first one
# 3. Out, file name and columns:
#    File: reading_log.csv
#    Columns: date, book_title, pages_read
# 4. Why these columns, and what this file is for:
#    I want to track how much I read. With 200 rows, I could compute how many pages
#    I read per month, which book took me the longest, and on which days I read the most.


# Your code below
print("Please fill in the following details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (DD/MM/YYYY): ")
student_number = input("Student Number: ")

with open("7.0_student_data.csv", "a", newline="") as file:
    file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

print("Data saved successfully!")