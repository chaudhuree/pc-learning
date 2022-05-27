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
