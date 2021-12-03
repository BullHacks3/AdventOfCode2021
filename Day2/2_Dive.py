x, y, aim = 0, 0, 0
for i in open("1_input.txt").read().splitlines():
    # separate out instruction and value : ins = forward , val = 5
    ins, val = i.split()
    if ins == "forward":
        x += int(val)
        y = y + aim*int(val)
    elif ins == "down":
        aim += int(val)
    elif ins == "up":
        aim -= int(val)

print(f"Answer: {x*y}")