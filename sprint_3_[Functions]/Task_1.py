"""Create function with name outer(name). This function should return inner function with name inner.
This inner function prints message Hello, <name>!
For example
tom = outer("tom")
tom() -> Hello, tom!"""

def outer(name):

    def inner():
        print("Hello, {}!".format(name))
    return inner