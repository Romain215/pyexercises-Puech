"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the data about one customer (the dictionary is written in the code).
# 2. Process: I read a field, change one, remove one, then go through all
#    the remaining fields.
# 3. Out: the values read, the modified field, the removed field,
#    then every remaining field with its value.
# 4. My object, my five fields, and why those: 
#    - name: to identify the customer.
#    - city: to choose where to deliver or which local campaign to run.
#    - monthly_budget: to plan how much we can spend on this customer.
#    - main_channel: to choose how to contact them.
#    - is_active: to know whether to include them in the next campaign.


# Your code below
name = input("Enter the customer name: ")
city = input("Enter the customer city: ")
budget = int(input("Enter the monthly budget: "))
channel = input("Enter the main channel: ")
is_active = True

customer = {
    "name": "Puech SARL",
    "city": "Albi",
    "monthly_budget": 1500,
    "main_channel": "email",
    "is_active": True
}

# Read fields
print("The customer's name is: ", customer["name"])
print("The customer's budget is: ", customer["monthly_budget"])

# Change a field
customer["monthly_budget"] = 1800
print("The new monthly budget is: ", customer["monthly_budget"])

# Remove a field
removed_channel = customer.pop("main_channel")
print("The removed field was: ", removed_channel)

# Display every remaining field with its value
for field, value in customer.items():
    print(field, ":", value)

# Check: asking for a field that does not exist
# print(customer["phone"])  -> KeyError, the program crashes
print(customer.get("phone", "This field does not exist"))