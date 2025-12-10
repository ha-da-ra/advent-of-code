dial = 50
zeroCount = 0
with open("input.txt") as file:
    for line in file:
        direction = -1 if line.startswith("L") else 1
        newDial =  dial + direction * int(line[1:])
        if newDial <=0:
            zeroCount += int(newDial / 100) * -1 + ( 1 if dial != 0 else 0)
        if newDial >= 100:
            zeroCount += int(newDial / 100)
        dial = newDial % 100
        print("afterRotation " + str(newDial))
        print("new " + str(dial))
        print("zeroCount " + str(zeroCount))

print(zeroCount)