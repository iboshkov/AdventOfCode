import re

with open('Day12.in', 'r') as f:
    data = f.readlines()

part_2 = True

if part_2:
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}    
else:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}

instructions = []

for line in data:
    instructions.append(line.strip().split())
i = 0
while i < len(instructions):
    instruction = instructions[i]
    name = instruction[0]
    args = instruction[1:]
    #print("Executign %s" % instruction)
    if name == "cpy":
        val = None
        try:
            val = int(args[0])
        except ValueError:
            val = registers[args[0]]
        registers[args[1]] = val
    if (name == "inc" or name == "dec") and args[0] != "0":
         #print("%s %s by 1" % (name, args[0]))
         registers[args[0]] += 1 if name == "inc" else -1
         #print(registers[args[0]])
    if (name == "jnz"):
        val = None
        try:
            val = int(args[0])
        except ValueError:
            val = registers[args[0]]
        if val != 0:
            i += int(args[1])
            continue
    i += 1
print(registers)