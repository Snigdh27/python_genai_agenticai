from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode!")

greet()