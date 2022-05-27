def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


# colorize([], 'cyan')
# colorize(34, "red")
print(colorize("Hello", "yellow"))

# example two
def user_name():
    name = input("Enter your name: ")
    if not name.isalpha():
        raise ValueError("Name must be alphabetic")
    return name


def printName():
    uname = user_name()
    print(f"Hello {uname}")


printName()
