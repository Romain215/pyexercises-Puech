# Romain Puech Garcia - Group CL10 
#
# 1. What goes in?
#    The file scenarios_C.csv. The separator is a comma. There are 14 columns:
#    Event (the situation), Day, Decision 1/2/3 (the text of options A, B, C),
#    Reputation 1/2/3, Budget 1/2/3, Outcome 1/2/3 (the feedback line).
#    Careful: Reputation comes BEFORE Budget in this file.
#    Numbers are written as text with a sign and a unit: "+15 pts", "-800 EUR", "+0 EUR".
#    I remove " pts" or " EUR" and convert the rest with int().
#    The impact of option B is in the columns "Reputation 2" and "Budget 2".
#    Some texts contain commas, so they are between quotes: the csv module handles that.
#
# 2. What happens? (one day)
#    - Show the day number, the budget and the reputation
#    - Show the situation and the options A, B, C
#    - Ask A, B or C until the answer is valid (lowercase accepted)
#    - Apply the budget and reputation change (reputation max 100)
#    - Show the feedback line and the changes
#    - Save the day in the history (a tuple)
#    - If budget or reputation is 0 or less: game over at once
#
# 3. What comes out?
#    At the end: fired (and why) or the final score and title,
#    then the best and worst move of the game.
#    One line is added to results.csv, for example:
#    Lea,11650,100,Viral Legend,2026-11-16
#
# 4. What could go wrong?
#    - The player types a wrong key (d, 1, nothing): the program asks again.
#    - A gauge goes below zero: the game stops at once and says "fired" and why.
#    - The scenario file is missing: the program shows an error message instead of crashing.
#    - results.csv does not exist the first time: the program creates it with a header line.
#    - Reputation goes above 100: it is capped at 100 with min().
#
# Feature chosen: d, Difficulty.
#    At the start, the player chooses easy (15,000 EUR) or hard (6,000 EUR).
#    I chose it because it changes the whole game with very little code,
#    so I keep time to make sure everything else runs without crashing.

import csv
import os
import random
from datetime import date

SCENARIO_FILE = "scenarios_C.csv"
RESULTS_FILE = "results.csv"
DAYS = 10
START_REPUTATION = 50
MAX_REPUTATION = 100


# Turn "+15 pts" or "-800 EUR" into a number (15 or -800)
def text_to_number(text):
    number = text.replace("pts", "").replace("EUR", "").strip()
    return int(number)


# Read the scenario file and return a list of scenarios
# Each scenario is a dictionary with the situation and a list of 3 option tuples
def load_scenarios(file_name):
    scenarios = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header line
        for row in reader:
            if len(row) < 14:
                continue  # skip empty or broken lines
            options = []
            for i in range(3):
                text = row[2 + i]
                reputation_change = text_to_number(row[5 + i])
                budget_change = text_to_number(row[8 + i])
                feedback = row[11 + i]
                options.append((text, budget_change, reputation_change, feedback))
            scenarios.append({"event": row[0], "options": options})
    return scenarios


# Ask easy or hard until the answer is valid, return the starting budget
def ask_difficulty():
    while True:
        answer = input("Difficulty, easy or hard? (E/H): ").strip().upper()
        if answer == "E":
            return 15000
        if answer == "H":
            return 6000
        print("Please type E or H.")


# Ask A, B or C until the answer is valid, return 0, 1 or 2
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ["A", "B", "C"]:
        answer = input("Please type A, B or C: ").strip().upper()
    return ["A", "B", "C"].index(answer)


# Apply one option to the gauges and return the new budget and reputation (a tuple)
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# Return the title that matches the final score
def get_title(score):
    if score >= 140:
        return "Viral Legend"
    elif score >= 120:
        return "CMO Material"
    elif score >= 95:
        return "Growth Hacker"
    else:
        return "Eternal Intern"


# Add one line to results.csv, with the header line the first time
def save_result(name, budget, reputation, title):
    file_is_new = not os.path.exists(RESULTS_FILE) or os.path.getsize(RESULTS_FILE) == 0
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file_is_new:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Main game
def play():
    name = input("Your name: ").strip()
    while name == "":
        name = input("Please type your name: ").strip()

    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("Error: the file", SCENARIO_FILE, "is missing.")
        return

    budget = ask_difficulty()
    reputation = START_REPUTATION
    random.shuffle(scenarios)
    history = []
    reason = ""

    # One loop turn = one day
    for day in range(1, DAYS + 1):
        scenario = scenarios[day - 1]
        print()
        print("--- Day", day, "---")
        print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
        print(scenario["event"])
        for letter, option in zip(["A", "B", "C"], scenario["options"]):
            print("  " + letter + ":", option[0])

        option = scenario["options"][ask_choice()]
        budget, reputation = apply_choice(budget, reputation, option)
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print("Budget", f"{budget_change:+}", "EUR, Reputation", f"{reputation_change:+}")
        history.append((reputation_change, day, text))

        # Game over as soon as a gauge is at 0 or less
        if budget <= 0:
            reason = "your budget hit zero"
            break
        if reputation <= 0:
            reason = "your reputation hit zero"
            break

    # End of the game: result, best and worst move, save
    print()
    print("==============================")
    if reason != "":
        print("You are fired:", reason + ".")
        title = "Fired"
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
        print("Final score:", score)
        print(name + ", your title:", title)

    best = max(history)
    worst = min(history)
    print()
    print("Best move:  day", best[1], '"' + best[2] + '"', f"({best[0]:+})")
    print("Worst move: day", worst[1], '"' + worst[2] + '"', f"({worst[0]:+})")

    save_result(name, budget, reputation, title)
    print("Saved in", RESULTS_FILE)


play()