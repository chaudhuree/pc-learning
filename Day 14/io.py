# file i/o system codes

f= open("D:\codes\python\pc-learning\Day 14\story.txt")
print(f.read()) # read the file
f.seek(4) # reset the cursor to the beginning of the file
print(f.read()) # read the file