# function definition
def my_function():
    print("ha"*9)


my_function()

# function with arguments


def my_name(fname):
    print(fname)


my_name("chaudhuree")

# function that multiply two numbers
# ternary operator used

def multiply(a, b):
    return "b cannot be zero" if b == 0 else a * b


answer = multiply(2, 3)
print(answer)
