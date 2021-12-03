with open("1_input.txt","r") as f:
    input1 = f.read().splitlines()

count = 0
temp = [int(input1[0]), int(input1[1]), int(input1[2])]
for i in range(3, len(input1)):
    initial_sum = sum(temp)
    temp = temp[1:] + [int(input1[i])]
    next_sum = sum(temp)
    if initial_sum < next_sum:
        count += 1

print(f"Answer is {count}")