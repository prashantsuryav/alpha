def decorator_function(original_function):
    print("Inside decorator")

    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("I am only displaying something ")


@decorator_function
def display_with_decorator():
    print("I am displaying something ")


# display()
# display_with_decorator()
decoratorFunction = decorator_function(display)
decoratorFunction()
