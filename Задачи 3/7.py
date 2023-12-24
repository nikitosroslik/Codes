def check_password_complexity(password):
    complexity_score = 0
    if len(password) >= 8:
        complexity_score += 1
    if any(char.isdigit() for char in password):
        complexity_score += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        complexity_score += 1
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        complexity_score += 1
    username = "username"
    if password.lower() != "password" and password.lower() != username.lower():
        complexity_score += 1
    return complexity_score
password = "Abc123"
score = check_password_complexity(password)
print(score)  
password = "password123"
score = check_password_complexity(password)
print(score)
