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

# ============== PART 3 ==============
# Write a function called get_top_students that helps teachers find their A-grade students!
# It should accept any number of student=score keyword arguments like colt=78 or elton=98
# It should return a list containing the names of students who scored 90 or above

# get_top_students(shahriar=91, kabir=83, sOhan=97, chaudhuree=69) -> ['shahriar', 'sOhan']
# get_top_students(sabrina=61, jahan=76) -------------------> []
# get_top_students(sadia=80, chaudhuree=95, simla=91)-----------> ['chaudhuree', 'simla']


def get_top_students(**kwargs):
    top_students = []
    for student, score in kwargs.items():
        if score >= 90:
            top_students.append(student)
    return top_students
print(get_top_students(shahriar=91, kabir=83, sOhan=97, chaudhuree=69))
