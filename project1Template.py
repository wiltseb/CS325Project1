'''
Reads data from input file
Returns list of list of ints
'''
def getInputData(filename):
    data = []
    with open(filename) as inFile:
        for line in inFile:
            line = line.split()
            line = [int(i) for i in line]
            data.append(line)
    return data



data = getInputData("MSS_TestProblems.txt")
print(data)


