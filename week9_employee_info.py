# IT 410 - Week 9 - Gathering and Validating Employee Information
# Name: Ahmed Gulam

import sys  # lets the program terminate (exit) as soon as bad input is found

# =====================================================
# Characters that are NOT allowed in each field
# =====================================================
bad_name_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
bad_email_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
bad_address_chars = '!"\'@$%^&*_=+<>?;:[]{}'

# =====================================================
# Employee ID: required, digits only, 7 digits or less
# =====================================================
employee_id = input("Enter the Employee ID: ").strip()

# isdigit() is False for empty text, letters, spaces, decimals and negatives,
# so this one test covers "required" and "must be a number"
if not employee_id.isdigit():
    print("Invalid Employee ID: it is required and must be a number.")
    sys.exit()  # stop the program without asking for more information

# Check the length rule (7 digits or less)
if len(employee_id) > 7:
    print("Invalid Employee ID: it must be 7 digits or less.")
    sys.exit()

# =====================================================
# Employee Name: required, mostly letters, no forbidden characters
# =====================================================
employee_name = input("Enter the Employee Name: ").strip()

# Required check
if employee_name == "":
    print("Invalid Employee Name: it is required.")
    sys.exit()

# Forbidden character check: look at every character in the name
for character in employee_name:
    if character in bad_name_chars:
        print(f"Invalid Employee Name: it cannot contain '{character}'.")
        sys.exit()

# "Primarily letters" check: count the letters, and require more than half
letter_count = 0
for character in employee_name:
    if character.isalpha():
        letter_count += 1
if letter_count <= len(employee_name) / 2:
    print("Invalid Employee Name: it must be primarily letters.")
    sys.exit()

# =====================================================
# Employee Email: required, mostly alphanumeric, no forbidden characters
# =====================================================
employee_email = input("Enter the Employee Email Address: ").strip()

# Required check
if employee_email == "":
    print("Invalid Email Address: it is required.")
    sys.exit()

# Forbidden character check
for character in employee_email:
    if character in bad_email_chars:
        print(f"Invalid Email Address: it cannot contain '{character}'.")
        sys.exit()

# "Primarily alphanumeric" check: count letters/digits, require more than half
alnum_count = 0
for character in employee_email:
    if character.isalnum():
        alnum_count += 1
if alnum_count <= len(employee_email) / 2:
    print("Invalid Email Address: it must be primarily letters and numbers.")
    sys.exit()

# =====================================================
# Employee Address: optional, but if given it is checked
# =====================================================
employee_address = input("Enter the Employee Address (optional, press Enter to skip): ").strip()

# Only validate the address if the user actually typed one
if employee_address != "":
    # Forbidden character check
    for character in employee_address:
        if character in bad_address_chars:
            print(f"Invalid Address: it cannot contain '{character}'.")
            sys.exit()

    # "Primarily alphanumeric" check (spaces and punctuation don't count)
    alnum_count = 0
    for character in employee_address:
        if character.isalnum():
            alnum_count += 1
    if alnum_count <= len(employee_address) / 2:
        print("Invalid Address: it must be primarily letters and numbers.")
        sys.exit()

# =====================================================
# Final message (all input was valid if we reach this point)
# =====================================================
message = (f"Hello, {employee_name}. Your Employee ID is {employee_id}, "
           f"and your email address is {employee_email}.")

# Choose the last sentence based on whether an address was provided
if employee_address != "":
    message += f" Your address is {employee_address}"
else:
    message += " You did not provide an address."

print(message)
