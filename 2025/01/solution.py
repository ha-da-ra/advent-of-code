dial = 50
zeroCount = 0
with open("input.txt") as file:
    for line in file:
        direction = -1 if line.startswith("L") else 1
        dial = (dial + direction * int(line[1:])) % 100
        if dial == 0:
            zeroCount += 1
        print(dial)

print(zeroCount)