#current position
depth = 0
horizontal = 0

def executeCommand(direction, amount):
    global depth
    global horizontal
    
    match direction:
        case "forward":
            horizontal = horizontal + amount
            print("Moved forward by", amount)
        case "up":
            depth = depth - amount
            print("Moved up by", amount)
        case "down":
            depth = depth + amount
            print("Moved down by", amount)

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

print("Final multiplied answer is", depth * horizontal)