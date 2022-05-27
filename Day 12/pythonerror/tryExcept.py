# THE BASIC SYNTAX:
# try:
# except:

# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "chaudhuree"}
print(get(d, "name"))
print(get(d, "city"))


# example 2:
# try:
# except:
# else:
# finally:


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")



# exmple 3:
# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")



# print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))
