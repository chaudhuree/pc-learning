with open("D:\codes\python\pc-learning\Day 14\write.txt", "w") as f:
    f.write("chaudhuree \n"*6)
# To write to a file, first open it in "w" mode
with open("./Day 14/haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# You can also write to files that don't yet exist
with open("./Day 14/lol.txt", "w") as file:
    file.write("haha" * 10)
