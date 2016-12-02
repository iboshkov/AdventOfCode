import code

with open('Day2.in', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
keypad = [  [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

class Hacker:
    x = 1
    y = 1
    buttons = []

    def __init__(self, kp):
        self.keypad = kp

    def do_command(self, cmd):
        keypad_size = len(self.keypad)-1

        if cmd == "U" and self.y > 0:
            self.y -= 1
        elif cmd == "D" and self.y < keypad_size:
            self.y += 1
        elif cmd == "L" and self.x > 0:
            self.x -= 1
        elif cmd == "R" and self.x < keypad_size:
            self.x += 1
    def remember_button(self):
        self.buttons.append((self.y, self.x))

h = Hacker(keypad)
for line in data:
    for command in line:
        h.do_command(command)
    h.remember_button()
