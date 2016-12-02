with open('Day2.in', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

keypad = [  [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

keypad_2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]

class Hacker:
    x = 0
    y = 0
    buttons = []

    def __init__(self, x, y, kp):
        self.keypad = kp
        self.x = x
        self.y = y
        self.buttons = []

    def is_valid(self, x, y):
        keypad_size = len(self.keypad)
        in_range = 0 <= x < keypad_size and 0 <= y < keypad_size
        return in_range and self.keypad[y][x] is not None

    def value(self, x, y):
        return self.keypad[y][x]

    def do_command(self, cmd):
        ox = self.x
        oy = self.y
        if cmd == "U":
            oy -= 1
        elif cmd == "D":
            oy += 1
        elif cmd == "L":
            ox -= 1
        elif cmd == "R":
            ox += 1
        if self.is_valid(ox, oy):
            self.x = ox
            self.y = oy

    def remember_button(self):
        self.buttons.append((self.x, self.y))

    def get_sequence(self):
        seq = []
        for button in self.buttons:
            seq.append(self.value(button[0], button[1]))
        return seq

h = Hacker(1, 1, keypad)
for line in data:
    for command in line:
        h.do_command(command)
    h.remember_button()

print(h.get_sequence())

h2 = Hacker(0, 2, keypad_2)
for line in data:
    for command in line:
        h2.do_command(command)
    h2.remember_button()
print(h2.get_sequence())
