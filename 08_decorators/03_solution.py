import time

def cache(func):    
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        print(f"Args is {args}")
        if args in cache_value:
            print(f"Cache Value is {cache_value[args]}")
            return cache_value[args]            
        result = func(*args)
        cache_value[args] = result
        print(f"Result is {result}")
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b

print(long_running_function(1, 2))
print(long_running_function(1, 2))
# print(long_running_function(2, 2))