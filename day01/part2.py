#array of all measurements
measurements = []

#fill up the measurements array
with open("day01/report.txt") as file:
    lines = file.readlines()
    for line in lines:
        #remove excess spaces
        number = line.strip()
        measurements.append(int(number))

#initialize array of sliding window
sums = []

#loop through all measurements
for i in range(len(measurements)):
    #skip first two
    if i < 2:
        continue
    
    #get sum of past three measurements
    sum = 0
    for j in range(3):
        sum = sum + measurements[i-j]
    
    #add sum to all sums
    sums.append(sum)

#answer to track
amountIncreased = 0

#loop through all sums
for i in range(len(sums)):
    #initialize line to print in console
    line = str(sums[i])

    #if first entry, don't compare
    if i == 0:
        line = line + " (N/A - no previous sum)"
    else:
        #compare to previous sums
        if sums[i] > sums[i-1]:
            amountIncreased += 1
            line = line + " (increased)"
        elif sums[i] == sums[i-1]:
            line = line + " (no change)"
        else:
            line = line + " (decreased)"
    #print line to console
    print(line)

#print answer
print("There are", amountIncreased, "sums that are higher than the previous ones") 