import time
import random
'''
Reads data from input file
Returns list of list of ints
Parameters:
filename - string name of file to open
'''
def getInputData(filename):
    data = []
    with open(filename) as inFile:
        for line in inFile:
            line = line.split()
            line = [int(i) for i in line]
            data.append(line)
    return data

'''
writes data to file in specified format
Parameters:
outFile - file object in write mode
A - full array
startPos - starting position of subArray
endPos - end position of subArray
total - sum of maximum subArray
'''
def writeData(outFile, A, startPos, endPos, total):
    outFile.write(" ".join(str(x) for x in A) + '\n')
    outFile.write(" ".join(str(A[x]) for x in range(startPos, endPos+1)) + '\n')
    outFile.write(str(total) + '\n\n')
    
'''
enumerative version of Max_Subarray
computes A[i] + A[i+1] + ... + A[j-1] + A[j] each time
Parameters:
A - an array of ints
outFile - file object in write mode
'''
def Enum_Max_Subarray(A):
    maximum = A[0]
    subArrayStart = 0
    subArrayEnd = 0
    currentTotal = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            currentTotal = 0
            for k in range (i, j+1):
                currentTotal += A[k]
                if currentTotal > maximum:
                    maximum = currentTotal
                    subArrayStart = i
                    subArrayEnd = j
    return [A, subArrayStart, subArrayEnd, maximum]

'''
Better enumerative version of Max_Subarray
stores prior computations of A[i] + A[i+1] + ... + A[j-1] 
Parameters:
A - an array of ints
outFile - file object in write mode
'''
def Better_Enum_Max_Subarray(A):
    maximum = A[0]
    subArrayStart = 0
    subArrayEnd = 0
    currentTotal = 0
    for i in range(len(A)):
        currentTotal = A[i]
        for j in range(i+1, len(A)):
            currentTotal += A[j]
            if currentTotal > maximum:
                maximum = currentTotal
                subArrayStart = i
                subArrayEnd = j
    return [A, subArrayStart, subArrayEnd, maximum]

def DCHelper(A):
    Divide_and_Conquer(A, 0, len(A) - 1)

def Divide_and_Conquer(A, low, high):
    if (low - high) == 0:
        return (A[low], A[low])
    else :
        #low = 0
        mid = (low + high) / 2
        #high = len(A)
        maxLeft = mid
        maxRight = mid + 1
        leftSum = 0
        rightSum = 0
        maxSum = 0
        for i in range(mid, low):
            maxSum = maxSum + A[i]
            if maxSum > leftSum:
                leftSum = maxSum
                maxLeft = i
        maxSum = 0
        
        for j in range(mid + 1, high):
            maxSum = maxSum + A[j]
            if maxSum > rightSum:
                rightSum = maxSum
                maxRight = j
        middleSum = leftSum + rightSum
        
        (leftSum, leftArray) = Divide_and_Conquer(A, low, mid)
        (rightSum, rightArray) = Divide_and_Conquer(A, mid + 1, high)
        
        maxSum = max(leftSum, rightSum, middleSum
        
        if(maxSum == leftSum):
                     return (leftArray, maxSum)
        elif(maxSum == rightSum)
                     return (rightArray, maxSum)
        elif(maxSum == middleSum):
                     return (A[maxLeft:maxRight + 1], maxSum)

'''
get time data from function with various input sizes
parameters:
functionToCall: function of algorithm you want to test
inputSizes: list of input sizes
'''
def timeFunction(functionToCall, inputSizes):
    testLists = []
    currList = []
    for i in inputSizes:
        for j in range(i):
            currList.append(random.randint(-1000, 1000))
        testLists.append(currList)
    timeList = []
    for i in range(len(testLists)):
        startTime = time.time()
        functionToCall(testLists[i])
        timeList.append(time.time() - startTime)
    return timeList

'''
print time data
Parameters:
function - name of function you want to call
inputSizes - list of inputSizes to test
'''
def getExperimentalData(function, inputSizes):
    timeList = timeFunction(function, inputSizes)
    print(str(function))
    for x in range(len(timeList)):
        print("n = " + str(enumInputSizes[x]) + ": " + str(timeList[x]))

'''
creates output file
parameters:
function - function of algorithm you want to call
inFilename - string of filename for input
outFilename - string of filename for output
'''
def createOutputFile(function, inFilename, outFilename):
    outFile = open(outFilename, 'w') #open outFile here so it overwrites existing file only once
    data = getInputData(inFilename)
    params = []
    for i in range(len(data)):
        params = function(data[i])
        #parameters for each function should be (outfile, originalArray, startPos, endPos, maximum)
        writeData(outFile, params[0], params[1], params[2], params[3])
    outFile.close()

'''    
enumInputSizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
betterEnumInputSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
'''
enumInputSizes = [50, 100, 150, 200, 250]
betterEnumInputSizes = [100, 200, 300, 400, 500]

#Gets experimental data for various n values for both enum functions
getExperimentalData(Enum_Max_Subarray, enumInputSizes)
getExperimentalData(Better_Enum_Max_Subarray, betterEnumInputSizes)

#takes in input file and writes results in specified file
createOutputFile(Enum_Max_Subarray, 'MSS_TestProblems.txt', 'outEnum.txt')
createOutputFile(Better_Enum_Max_Subarray, 'MSS_TestProblems.txt', 'outBE.txt')





