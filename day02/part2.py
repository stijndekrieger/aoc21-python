#current position
depth = 0
horizontal = 0
aim = 0

def executeCommand(direction, amount):
    global depth
    global horizontal
    global aim
    
    match direction:
        case "forward":
            horizontal = horizontal + amount
            print("Moved forward by", amount)
            if aim != 0:
                depth = depth + (aim * amount) 
                print("Depth changed by", amount)
        case "up":
            aim = aim - amount
            print("Pointed up by", amount)
        case "down":
            aim = aim + amount
            print("Pointed down by", amount)

#execute all commands
with open("day02/commands.txt") as file:
    lines = file.readlines()
    for line in lines:
        #remove excess spaces
        command = line.strip()

        #get direction and amount and execute command
        direction = command.split()[0]
        amount = int(command.split()[1])
        executeCommand(direction, amount)

print("Depth is", depth, "and horizontal is", horizontal)
print("Final multiplied answer is", depth * horizontal)