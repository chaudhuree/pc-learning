def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    if phrase.startswith(interrogatives):
        capitalized = phrase.capitalize()
        return f"{capitalized}?"
    else:
        return f"{phrase}."


results = []
while True:
    user_input = input("Say something >>> ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
print(" ".join(results))
