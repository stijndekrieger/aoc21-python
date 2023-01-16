gamma = ""
epsilon = ""
bits = []

with open("day03/report.txt") as file:
    lines = file.readlines()
    for line in lines:
        bit = line.strip()
        bits.append(bit)

maxLength = len(bits[0])
for i in range(maxLength):
    amountOfOne = 0
    amountOfZero = 0

    for bit in bits:
        if int(bit[i]) == 1:
            amountOfOne += 1
        elif int(bit[i]) == 0:
            amountOfZero += 1
    
    if amountOfZero > amountOfOne:
        gamma += "0"
        epsilon += "1"
    elif amountOfOne > amountOfZero:
        gamma += "1"
        epsilon += "0"
    
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print("Gamma rate is", gamma, "and Epsilon is", epsilon)
print("Power consumption is", gamma * epsilon)