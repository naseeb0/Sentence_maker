def sentence_maker(phrase):
    upp_maker = phrase.title()
    interrogative = ("why", "how", "what", "when","where")
    if phrase.startswith(interrogative):
        return f"{upp_maker}?"
    else:
        return f"{upp_maker}."
    
results = []    
while True:
    u_name = input("Say Something: ")
    if u_name == "\end":
        break
    else:
        results.append(sentence_maker(u_name))

print(" ".join(results))
