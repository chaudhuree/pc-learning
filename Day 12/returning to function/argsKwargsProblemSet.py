# ============== PART 1 ==============
# Write a function called contains_pickle that accepts any number of arguments.
# The function should return True if it is passed "pickle" as one of the args
# Otherwise it should return False

#  contains_pickle("red", 45, "pickle", [])  --> True
#  contains_pickle(1,2, "blue") ---------------> False
def contains_pickle(*args):
    return "pickle" in args


print(contains_pickle("red", 45, "pickle", []))

# ============== PART 2 ==============
# Write a function called count_fails that counts up the number of failing test scores it is passes
# It should accept any number of arguments
# It should return a count of how many args are less than or equal to 50

# count_fails(99,48,79,36) -------> 2
# count_fails(85,78,91) ----------> 0
# count_fails(50,41,47,74,76,81) -> 3


def count_fails(*scores):
    count = 0
    for score in scores:
        if score <= 50:
            count += 1
    return count


print(count_fails(50, 41, 47, 74, 76, 81))
