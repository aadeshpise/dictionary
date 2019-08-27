import json
from difflib import get_close_matches

dictionary = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in dictionary:
        return dictionary[w]
    elif len(get_close_matches(w, dictionary.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, dictionary.keys())[0])
        if yn == "Y":
            return dictionary[get_close_matches(w, dictionary.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
         print(item)
else:
    print(output)
