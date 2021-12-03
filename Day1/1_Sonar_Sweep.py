"""
Problem: Sonar Sweep
"""

with open("1_input.txt","r") as f:
    input1 = f.read().splitlines()

count = 0
for i in range(1,len(input1)):
    if int(input1[i]) > int(input1[i-1]):
        count += 1

print(f"Answer for Sonar sweep problem is {count}")


