# Copy
# Copy should copy contents from one file to another.  For example, after running:


def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)


copy('D:\codes\python\pc-learning\Day 14\exercise i\o\story.txt',
     'D:\codes\python\pc-learning\Day 14\exercise i\o\story_copy.txt')
