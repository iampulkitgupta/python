password = "awedkshbdfje453we"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
elif len(password) > 10:
    strength = "Strong"
    
print(f"Your password is {strength}")