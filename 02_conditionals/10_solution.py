Pet = "Cat"
Age = 6
food = ""

if Pet == "Dog":
    if Age < 2:
        food = "Puppy food"
elif Pet == "Cat":
    if Age > 5:
        food = "Senior Cat food"

print(f"Recommended {Pet} food is {food}")