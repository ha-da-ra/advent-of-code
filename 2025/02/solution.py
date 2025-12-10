invalidIdSum = 0
with open("input.txt") as file:
    ranges = file.readline().split(",")
    for range in ranges:
        print(range)
        dashIndex = range.index("-")
        start = int(range[:dashIndex])
        end = int(range[dashIndex +1:])
        firstHalf = str(start)[:len(str(start))//2]
        if firstHalf == '':
            firstHalf = '0'
        sillyNumber = int(firstHalf + firstHalf)
        while sillyNumber <= end:
            if sillyNumber >= start:
                invalidIdSum  = invalidIdSum + sillyNumber
                print(sillyNumber)
            firstHalf = str(int(firstHalf) + 1)
            sillyNumber = int(firstHalf + firstHalf)
print(invalidIdSum)
   
#24747430232