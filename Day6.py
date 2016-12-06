from itertools import groupby
import operator

columns = []

with open('Day6.in', 'r') as f:
    data = f.readlines()
    for line in (data):
        for i, c in enumerate(line.strip()):
            if len(columns) < i+1:
                columns.append([])
            columns[i].append(c)

ld = [groupby(sorted(c)) for c in columns]

message = ""
real_message = ""
for d in ld:
    occurences = {k : len(list(v)) for k, v in d}
    sorted_occurences = sorted(occurences.items(), key=operator.itemgetter(1), reverse=True)
    message += str(sorted_occurences[0][0])
    real_message += str(sorted_occurences[-1][0])

print(message)
print(real_message)