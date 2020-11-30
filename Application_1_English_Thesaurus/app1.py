import json
from difflib import get_close_matches   # Similarity Ratio Between TwoWords

# loading JSON data
data = json.load(open("data.json"))     # global var

def translate(w):                       # local var
    w = w.lower()                       # letter case
    # return the definition of a word
    if w in data:
        return data[w]
    elif w.title() in data:             # check for proper nouns (e.g., Texas, Delhi)
        return data[w.title()]
    elif w.upper() in data:             # check for acronyms (e.g., USA, NATO)
        return data[w.upper()]
    # recommending the best match
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn in ["Y", "yes"]:
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":                 # confirmation from the user
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    # non-existing words
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")            # global var

output = translate(word)

if type(output) == list:                # optimize output
    for item in output:
        print(item)
else:
    print(output)