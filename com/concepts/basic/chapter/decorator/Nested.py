def second_func(first_function):
    print("I'm in second func")

    def wrapper_func():
        print("I'm in wrapper func: ")
        return first_function()
    return wrapper_func


def first_func():
    print("I'm in first func")


c = second_func(first_func)
c()