#array of all measurements
measurements = []

#fill up the measurements array
with open("day01/report.txt") as file:
    lines = file.readlines()
    for line in lines:
        #remove excess spaces
        number = line.strip()
        measurements.append(int(number))

#answer to track
amountIncreased = 0

#loop through all measurements
for i in range(len(measurements)):
    #initialize line to print in console
    line = str(measurements[i])

    #if first entry, don't compare
    if i == 0:
        line = line + " (N/A - no previous measurement)"
    else:
        #compare to previous measurement
        if measurements[i] > measurements[i-1]:
            amountIncreased += 1
            line = line + " (increased)"
        elif measurements[i] == measurements[i-1]:
            line = line + " (no change)"
        else:
            line = line + " (decreased)"
    #print line to console
    print(line)

#print answer
print("There are", amountIncreased, "measurements that are higher than the previous ones")
