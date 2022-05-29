# file i/o system codes

f= open("D:\codes\python\pc-learning\Day 14\story.txt")
print(f.read()) # read the file
print('\n')
f.seek(4) # reset the cursor to the second word of the file
print(f.read()) # read the file
print('\n')
f.seek(0) # reset the cursor to the beginning of the file
print(f.readline()) # read the first line of the file
f.seek(0) # reset the cursor to the beginning of the file
print('\n')
print(f.closed) # check if the file is closed
f.close() # close the file
print(f.closed) # check if the file is closed