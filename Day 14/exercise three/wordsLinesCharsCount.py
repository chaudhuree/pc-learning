# Statistic Exercise Solution

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            "characters": sum(len(line) for line in lines)}


data = statistics(
    "D:\codes\python\pc-learning\Day 14\exercise three\\text.txt")

print(data)
