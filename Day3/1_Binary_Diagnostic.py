f = open("1_input.txt")
data = f.read().splitlines()
f.close()

temp = [{"0":0, "1":0} for _ in range(len(data[0]))]

for number in data:
    for index, digit in enumerate(number):
        temp[index][digit] += 1

gamma_rate = ""
epsilon_rate = ""
for check in temp:
    if check.get("0") > check.get("1"):
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

print(f"Answer: {int(gamma_rate,2)*int(epsilon_rate,2)}")