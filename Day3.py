with open('Day3.in', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

def valid_triangle(triangle):
    a = triangle[0] + triangle[1] > triangle[2]
    b = triangle[1] + triangle[2] > triangle[0]
    c = triangle[0] + triangle[2] > triangle[1]

    return a and b and c

valid_rows = 0
valid_columns = 0

triangles = [[], [], []]
for line in data:
    sides = [float(side.strip()) for side in line.split()]

    # part 2
    for i in range(3):
        triangles[i].append(sides[i])
        if len(triangles[i]) % 3 == 0:
            if valid_triangle(triangles[i]):
                valid_columns += 1
            triangles[i] = []
    # Part 1
    if valid_triangle(sides):
        valid_rows += 1

print("Valid by rows: %d" % valid_rows)
print("Valid by columns: %d" % valid_columns)
