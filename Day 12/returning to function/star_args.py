def addition(*args):
    total = 0
    for num in args:
        total += num
    return total


print(addition(1, 2, 3, 4, 5))
print(addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# example two


def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Note sure who you are"


print(ensure_correct_info("hello", False, 78))  # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))
