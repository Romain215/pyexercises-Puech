"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three pieces of text typed by the user: a username, an email address
#    and a French phone number.
# 2. Process: spaces at the start and end are removed, then each value is
#    checked against its own pattern with re.fullmatch() (the WHOLE value must
#    match, not just a part of it).
# 3. Out: a message for each field saying if it is valid or not. Only if all
#    three are valid, the values are saved as one line in "saved_entries.txt".
#    If even one is invalid, nothing is saved.
#
# 4. The three fields and their rules, in plain English:
#
#    USERNAME
#      Accept: 3 to 15 characters, only letters (no accents), digits and
#      underscores "_", and it must start with a letter.
#      Reject: spaces, symbols like "-" or "@", starting with a digit, too
#      short or too long.
#      Borderline case: "Bob_" is accepted. Ending with "_" looks odd, but it
#      is harmless, so I allow it.
#
#    EMAIL
#      Accept: some characters before one "@", then a domain name, then a dot
#      and an extension of at least 2 letters (".fr", ".com").
#      Before the "@": letters, digits and . _ % + -
#      Domain: letters, digits and "-", possibly several parts separated by
#      dots ("mail.univ-paris.fr").
#      Reject: no "@", two "@", spaces, no extension, an extension of 1 letter.
#      Borderline case: I do NOT check that the address really exists. I only
#      check its shape. Checking existence needs to send an email.
#
#    PHONE (French mobile or landline, written without spaces)
#      Accept: exactly 10 digits, starting with 0, and the second digit is
#      1 to 9 (e.g. 0612345678).
#      Reject: letters, fewer or more than 10 digits, starting with "00",
#      spaces or dots between the digits, the +33 format.
#      Borderline case: "06 12 34 56 78" (with spaces) is rejected. I chose
#      a strict format to keep the pattern simple; the user is told to type
#      the digits without spaces.
#
# Why separate checks instead of one: each field gets its own message, so the
# user knows exactly which value to fix.
#
# CHECK IT YOURSELF: the 9 test values (1 pass + 2 fail per field) are in
# TEST_CASES below and run automatically when the program starts.
# Results (all 9 behaved as expected):
#    username  "alice_92"        -> valid
#    username  "9alice"          -> invalid (starts with a digit)
#    username  "al"              -> invalid (too short)
#    email     "alice@mail.fr"   -> valid
#    email     "alice.mail.fr"   -> invalid (no @)
#    email     "alice@mail"      -> invalid (no extension)
#    phone     "0612345678"      -> valid
#    phone     "06123"           -> invalid (too short)
#    phone     "06 12 34 56 78"  -> invalid (spaces)
#
# Surprise: "alice..bob@mail.fr" (two dots in a row) is ACCEPTED by my email
# pattern, because "." is allowed before the "@" and nothing forbids two in a
# row. Real email systems usually refuse it. I keep my pattern simple and
# accept this limit.


import re

# ---------------------------------------------------------------------------
# PATTERNS, explained piece by piece
# ---------------------------------------------------------------------------

# USERNAME:  [A-Za-z][A-Za-z0-9_]{2,14}
#   [A-Za-z]          -> exactly one letter (lowercase or uppercase): the first
#                        character must be a letter.
#   [A-Za-z0-9_]      -> one letter, digit or underscore...
#   {2,14}            -> ...repeated between 2 and 14 times.
#   Total: 1 + (2 to 14) = 3 to 15 characters.
USERNAME_PATTERN = r"[A-Za-z][A-Za-z0-9_]{2,14}"

# EMAIL:  [A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}
#   [A-Za-z0-9._%+-]+     -> the part before @: one or more ("+") letters,
#                            digits or . _ % + -
#   @                     -> exactly one "@".
#   [A-Za-z0-9-]+         -> the first part of the domain ("mail").
#   (\.[A-Za-z0-9-]+)*    -> optional extra parts, each starting with a dot
#                            (".univ-paris"); "*" means zero or more times.
#                            "\." is a real dot: without "\", "." means
#                            "any character".
#   \.                    -> the dot before the extension.
#   [A-Za-z]{2,}          -> the extension: at least 2 letters ("fr", "com").
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

# PHONE:  0[1-9][0-9]{8}
#   0                 -> the first digit must be 0.
#   [1-9]             -> the second digit is 1 to 9 (so "00..." is refused).
#   [0-9]{8}          -> exactly 8 more digits.
#   Total: 1 + 1 + 8 = 10 digits.
PHONE_PATTERN = r"0[1-9][0-9]{8}"

# re.fullmatch() is used instead of re.match() or re.search(): the pattern
# must cover the WHOLE value. With re.search(), "xx0612345678xx" would pass
# because a valid phone number is hidden inside it.

FIELDS = [
    ("username", USERNAME_PATTERN, "3-15 letters, digits or _, starting with a letter"),
    ("email", EMAIL_PATTERN, "like name@domain.fr"),
    ("phone", PHONE_PATTERN, "10 digits starting with 0, no spaces (e.g. 0612345678)"),
]

TEST_CASES = [
    ("username", "alice_92", True),
    ("username", "9alice", False),
    ("username", "al", False),
    ("email", "alice@mail.fr", True),
    ("email", "alice.mail.fr", False),
    ("email", "alice@mail", False),
    ("phone", "0612345678", True),
    ("phone", "06123", False),
    ("phone", "06 12 34 56 78", False),
]

SAVE_FILE = "saved_entries.txt"


def is_valid(pattern, value):
    """Return True if the WHOLE value matches the pattern."""
    return re.fullmatch(pattern, value) is not None


def run_tests():
    """Run the 9 test values and show if each one behaves as expected."""
    patterns = {name: pattern for name, pattern, _ in FIELDS}
    print("=== Test run (9 values) ===")
    for field, value, expected in TEST_CASES:
        result = is_valid(patterns[field], value)
        status = "OK" if result == expected else "SURPRISE"
        print(f"{status:9} {field:9} {value!r:20} -> {'valid' if result else 'invalid'}")
    print()


def main():
    run_tests()

    print("=== Enter your information ===")
    values = {}
    all_valid = True

    for name, pattern, hint in FIELDS:
        value = input(f"{name.capitalize()}: ").strip()
        values[name] = value
        if is_valid(pattern, value):
            print(f"  OK: valid {name}.")
        else:
            print(f"  Invalid {name}. Expected: {hint}.")
            all_valid = False

    if all_valid:
        with open(SAVE_FILE, "a", encoding="utf-8") as f:
            f.write(f"{values['username']};{values['email']};{values['phone']}\n")
        print(f"\nAll three values are valid. Saved to {SAVE_FILE}.")
    else:
        print("\nAt least one value is invalid. Nothing was saved.")


main()
