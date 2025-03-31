# Problem 2: Debugging Function Calls

 #Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        args_values = ", ".join(str(arg) for arg in args  )
        kwargs_values = ", ".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling {function_name} with no of args is {args_values} and no of kwargs is {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("hello")
@debug
def greeting(name, greet = "hello"):
    print(f"{greet}, {name}")

hello()
greeting("garvit", greet="hanji")