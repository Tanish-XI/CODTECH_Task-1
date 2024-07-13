import re

# Common password comparison list
COMMON_PASSWORDS = set()
with open('common_passwords.txt') as f:
    for line in f:
        COMMON_PASSWORDS.add(line.strip())

def assess_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("Password length is good.")
    elif len(password) >= 8:
        score += 1
        feedback.append("Password length is acceptable.")
    else:
        feedback.append("Password is too short.")

    # Check for complexity
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Check for common passwords
    if password in COMMON_PASSWORDS:
        score = 0
        feedback = ["Password is too common. Choose a more unique password."]

    # Assessments
    if score == 6:
        feedback.append("Password is very strong.")
    elif score >= 4:
        feedback.append("Password is strong.")
    elif score >= 2:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")

    return score, feedback

if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    score, feedback = assess_password_strength(password)
    print(f"Password Score: {score}/6")
    for comment in feedback:
        print(f"- {comment}")
