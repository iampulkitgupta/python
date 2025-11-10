age = 17
day = "Wednesday"


price = 12 if age>= 18 else 8
discount = 2 if day == "Wednesday" else 0

final_price = price - discount
print(f"Ticket price for you is ${final_price}")    

