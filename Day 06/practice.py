# check even or odd numbers
def evenly(num):
    return "even" if num % 2 == 0 else "odd"

answer=evenly(2)
print (answer)
answer=evenly(5)
print (answer)

# function to convery slugify string
def slugify(str):
    return str.lower().strip().replace(" ", "-")

print(slugify("Hello World"))

# count vowels in a string
def vowels(str):
    count = 0
    for letter in str:
        if letter in "aeiou":
            count += 1
    return count
print("number of vowels: ",vowels("shahriar kabir sohan chaudhuree"))
print("number of vowels: ",vowels("kazi sabrina jahan easha"))