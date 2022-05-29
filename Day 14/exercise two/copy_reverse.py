# Copy and Reverse

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])


copy_and_reverse("D:\codes\python\pc-learning\Day 14\exercise two\story.txt",
                 "D:\codes\python\pc-learning\Day 14\exercise two\story_reverse.txt")
