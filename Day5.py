import hashlib
id = "ffykfhsq"
num_zeros = 5
password_length = 8
found_characters_1 = []
found_characters_2 = []
i = 0
while len(found_characters_1) < password_length or len(found_characters_2) < password_length:
    m = hashlib.md5()
    m.update(id + str(i))
    hashed = m.hexdigest()

    if hashed.startswith("0" * num_zeros):
        c = hashed[num_zeros]
        c_2 = hashed[num_zeros+1]
        print("[Part 1] Iteration %d: Character in hash %s: %s" % (i, hashed, c))
        print("[Part 2] Iteration %d: Character in hash %s: %s at position %s" % (i, hashed, c_2, c))
        found_characters_1.append(c)
    i += 1
print("".join(found_characters_1))
print("".join(found_characters_2))
