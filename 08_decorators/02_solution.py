def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)        
    return wrapper



@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice", greeting="Hi"))
print(greet("Bob"))
