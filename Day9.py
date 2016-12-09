import re

with open('Day9.in', 'r') as f:
    data = f.readlines()[0]

# (\((\d+)x(\d+)\))
markers = re.compile(r"(\((\d+)x(\d+)\))")
def decompress(d, part=1):
    # print("decompressing '%s' " % d)
    match = markers.search(d)
    if match is None:
        return len(d)
    param1 = int(match.group(2))
    param2 = int(match.group(3))
    start = match.start()
    end = match.end()

    multiplier = param1 if part == 1 else  decompress(d[end : end + param1], part)

    return start + param2 * multiplier + decompress(d[end+param1:], part)
c = decompress(data)

print(c)