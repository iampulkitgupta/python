number = 29

is_prime = True

if number > 1:
    for num in range(2, number):
        if (number % num) == 0:
            is_prime = False
            break

print(f"is {number} number prime? {is_prime}")