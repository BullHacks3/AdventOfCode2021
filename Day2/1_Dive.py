x, y = 0,0
for i in open("1_input.txt").read().splitlines():
    # separate out instruction and value : ins = forward , val = 5
    ins, val = i.split()
    if ins == "forward":
        x += int(val)
    elif ins == "down":
        y += int(val)
    elif ins == "up":
        y -= int(val)

print(f"Answer: {x*y}")