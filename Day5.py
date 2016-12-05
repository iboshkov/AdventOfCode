import hashlib
id = "ffykfhsq"
num_zeros = 5
password_length = 8
found_characters_1 = []
found_characters_2 = [None] * password_length
i = 0
while len(found_characters_1) < password_length or None in found_characters_2:
    m = hashlib.md5()
    m.update((id + str(i)).encode("utf-8"))
    hashed = m.hexdigest()

    if hashed.startswith("0" * num_zeros):
        c = hashed[num_zeros]
        c_2 = hashed[num_zeros+1]
        print("[Part 2] Iteration %d: Character in hash %s: %s at position %s" % (i, hashed, c_2, c))
        try:
            idx = int(c)
            if idx < password_length and found_characters_2[idx] is None:
                found_characters_2[idx] = c_2
        except ValueError:
            pass
        if len(found_characters_1) < password_length:
            print("[Part 1] Iteration %d: Character in hash %s: %s" % (i, hashed, c))
            found_characters_1.append(c)
    i += 1
print("".join(found_characters_1))
print("".join(found_characters_2))
