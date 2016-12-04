from itertools import groupby
import operator

alphabet = "abcdefghijklmnopqrstuvwxyz"

with open('Day4.in', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

num_valid = 0
sum_sectors = 0
valid_names = set()

for line in data:
    line_split = line.split("-")
    checksum_split = line_split[-1].split("[")
    sector_id = int(checksum_split[0])
    checksum = checksum_split[-1][:-1]
    d = groupby(sorted("".join(line_split[:-1])))

    occurences = {k : len(list(v)) for k, v in d}
    s = sorted(occurences.items(), key=operator.itemgetter(0))
    s = sorted(s, key=operator.itemgetter(1), reverse=True)

    calculated_checksum = "".join([x[0] for x in s])

    valid = checksum in calculated_checksum
    name_only = " ".join(line_split[:-1])
    processed = "".join([alphabet[(ord(c) - 97 + sector_id) % len(alphabet)]
        if c.isalpha() else " " for c in name_only])
    if valid:
        num_valid += 1
        sum_sectors += sector_id
        valid_names.add((processed, sector_id))

print("Valid: %d" % num_valid)
print("Sum of valid sectors: %d" % sum_sectors)
print("-" * 64)
for name in valid_names:
    print(name)
