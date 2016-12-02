with open('Day1.in', 'r') as f:
    data = f.read()

def dist(x, y):
    return (x[0] - y[0]) + (x[1] - y[1])

class Walker:
    angle = 90

    path = [(0, 0)]

    x = 0
    y = 0

    repeated_self = False
    first_repeat_distance = 0

    def dir(self):
        if self.angle == 90:
            return ("N", 0, -1)
        elif self.angle == 0:
            return ("E", 1, 0)
        elif self.angle == 180:
            return ("W", -1, 0)
        elif self.angle == 270:
            return ("S", 0, 1)

    def get_path_distance(self):
        d = 0
        for i in range(0, len(self.path)-1):
            a = self.path[i]
            b = self.path[i+1]
            d += dist(a, b)
        return abs(d)

    def turn(self, d):
        da = -90 if d == "R" else 90
        self.angle += da
        self.angle = self.angle % 360

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        new_pos = (self.x, self.y)

        first_repetition = False
        if new_pos in self.path and not self.repeated_self:
            self.repeated_self = True
            first_repetition = True

        self.path.append(new_pos)

        if first_repetition:
            self.first_repeat_distance = self.get_path_distance()

    def walk(self, amount):
        d = self.dir()
        dx = amount * d[1]
        dy = amount * d[2]
        while dx != 0:
            self.move(d[1], 0)
            dx -= d[1]
        while dy != 0:
            self.move(0, d[2])
            dy -= d[2]

    def walk_sequence(self, sequence):
        for i in sequence.split(", "):
            dist = int(i[1:])
            dir = i[0]
            w.turn(dir)
            w.walk(dist)
        return w.get_path_distance(), w.first_repeat_distance

w = Walker()

result = w.walk_sequence(data)

print("Full distance: %d, first repetition: %d" % result)
