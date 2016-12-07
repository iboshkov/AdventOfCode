import re

with open('Day7.in', 'r') as f:
    data = f.readlines()

abba = re.compile(r"(.)(.)\2\1")

amount = 0

for line in data:
    all = re.findall(r"\w+", line)

    hypernet = re.findall(r"(\[)(\w+)(\])", line);
    hypernet = [y for tup in hypernet for y in tup]
    
    valid = False
    for word in all:
        match = abba.search(word)
        if match is not None:
            start = match.start()
            if word in hypernet:
                valid = False
                print(word)
                print(match)
                print("Abba in hypernet");
                break

            if word[start] == word[start+1]:
                continue
            print(word)
            print(match)
            valid = True
    if valid:
        amount += 1
        
        print("Matched", line)            
print(amount)