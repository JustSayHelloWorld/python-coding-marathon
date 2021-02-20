"""Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.

For example

print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo"""


def logger(func):
    def wrapper(*args, **kwargs):

        func_arguments = []

        if len(args) > 0:
            for each in args:
                func_arguments.append(each)
        if len(kwargs) > 0:
            for each in kwargs:
                func_arguments.append(kwargs[each])

        function = func(*args, **kwargs)

        print(f"Executing of function {func.__name__} with arguments", end=" ")
        for i in range(len(func_arguments)):

            if i < len(func_arguments) - 1:
                print(func_arguments[i], end=", ")
            else:
                print(func_arguments[i], end="")
        print("...")

        return function  

    return wrapper


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


@logger
def concat(*args, **kwargs):
    concated = ""

    if len(args) > 0:
        for each in args:
            concated += str(each)
    if len(kwargs) > 0:
        for each in kwargs:
            concated += str(kwargs[each])

    return concated