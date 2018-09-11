import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Press Y for yes, N for no: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Sry that word doesn't exist."
        else:
            return "Sry don't understand you."
    else:
        return "Sry, not in there."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
