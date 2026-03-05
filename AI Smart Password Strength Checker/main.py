import re

def check_password_strength(password):
    score = 0
    remarks = []

    ############-Length check-###############
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters")

    ###########-Uppercase-##########
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter")

    ########-Lowercase-##########
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter")

    ##########-Digit-#########
    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add at least one number")

    ########-Special character-########
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character")

    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, remarks


password = input("Enter your password: ")

strength, remarks = check_password_strength(password)

print("\nPassword Strength:", strength)

if remarks:
    print("\nSuggestions:")
    for r in remarks:
        print("-", r)
