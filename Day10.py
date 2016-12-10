import re

with open('Day10.in', 'r') as f:
    data = f.readlines()

init_commands = []
giving_commands = []

class Actor:
    def __init__(self, name):
        self.name = name
        self.chips = []
        self.giving_log = []
    
    def receive_chip(self, val):
        self.chips.append(val)

    def can_give(self):
        return len(self.chips) >= 2

    def give_chip(self, target, high):
        chips = sorted(self.chips, reverse=high)
        if len(chips) == 0:
            return
        chip_to_give = max(chips) if high else min(chips)
        self.chips.remove(chip_to_give)
        target.receive_chip(chip_to_give)
    
    def __repr__(self):
        return "\nname: '" + self.name + "'\nchips: " + str(self.chips) + "\n"

output = Actor("Output")
bots = {}

for line in data:
    line = line.strip()
    if "goes" in line:
        init_commands.append(line)
    elif "gives" in line:
        giving_commands.append(line)
    else:
        print("Wat")

input_no = 1
for command in init_commands:
    args = command.split()
    bot_name = " ".join(args[4:])
    val = int(args[1])
    bot = None
    if bot_name in bots:
        bot = bots[bot_name]
    if bot is None:
        bot = Actor(bot_name)
    bot.receive_chip(val)
    input_no += 1
    bots[bot.name] = bot

target_bot = None

finished = False
while not finished:
    finished = True
    for command in giving_commands:
        args = command.split()
        main_actor_name = " ".join(args[:2])

        if main_actor_name not in bots:
            continue
        else:
            main_actor = bots[main_actor_name]

        if not main_actor.can_give():
            continue
        
        # This bot can give chips, not over yet.
        finished = False

        high_actor_name = " ".join(args[-2:])
        low_actor_name = " ".join(args[5:7])

        if low_actor_name not in bots:
            low_actor = Actor(low_actor_name)
            bots[low_actor.name] = low_actor
        else:
            low_actor = bots[low_actor_name]

        if high_actor_name not in bots:
            high_actor = Actor(high_actor_name)
            bots[high_actor.name] = high_actor
        else:
            high_actor = bots[high_actor_name]

        main_actor.give_chip(low_actor, False)
        main_actor.give_chip(high_actor, True)
        for bot in bots.values():
            if 17 in bot.chips and 61 in bot.chips:
                target_bot = bot

print("Target bot: %s" % target_bot.name)
out = 1
for i in range(0, 3):
    out *= bots["output %d" % i].chips[0]
print("Multiplying output 0 1 and 2: %d" % out)