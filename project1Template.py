import time
import random
from math import floor
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
    outFile.write(' '.join(str(x) for x in A) + '\n')
    outFile.write(' '.join(str(A[x]) for x in range(startPos, endPos+1)) + '\n')
    outFile.write(str(total) + '\n\n')
    
'''
enumerative version of Max_Subarray
computes A[i] + A[i+1] + ... + A[j-1] + A[j] each time
Parameters:
A - an array of ints
Returns - array consisting of original array, startPositon of subarray, endPositon of subArray, and maximum subarray sum
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
Returns - array consisting of original array, startPositon of subarray, endPositon of subArray, and maximum subarray sum

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
    return Divide_and_Conquer(A, 0, len(A) - 1)

def Divide_and_Conquer(A, low, high):
    '''if (low - high) == 0:
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
        
        maxSum = max(leftSum, rightSum, middleSum)
        
        if(maxSum == leftSum):
                     return (maxSum, leftArray)
        elif(maxSum == rightSum):
                     return (maxSum, rightArray)
        elif(maxSum == middleSum):
                     return (maxSum, A[maxLeft:maxRight + 1])
<<<<<<< HEAD
<<<<<<< HEAD
'''
    #rightHigh = 0
    #leftHigh = 0
    #leftSum = 0
    #RightSum = 0
    #crossLow = 0
    #crossHigh = 0
    if high == low:
        return[A, low, high, A[low]]
    else: 
	mid = ((low + high) / 2)
    	(A, leftLow, leftHigh, leftSum) = Divide_and_Conquer(A, low, mid)
    	(A, rightLow, rightHigh, rightSum) = Divide_and_Conquer(A, mid + 1, high)
    	(A, crossLow, crossHigh, crossSum) = maxCrossing(A, low, mid, high)
               
    	if (leftSum >= rightSum and leftSum >= crossSum):
               return[A, leftLow, leftHigh, leftSum]
    	elif (rightSum >= leftSum and rightSum >= crossSum):
               return[A, rightLow, rightHigh, rightSum]
   	else: 
               return[A, crossLow, crossHigh, crossSum]
             
def maxCrossing(A, low, mid, high):
	leftSum = float("-inf")
     	sum = 0
	maxRight = 0
	maxLeft = 0
     	for i in range(mid, low - 1, -1):
        	sum = sum + A[i]
        	if sum > leftSum:
        		leftSum = sum
        		maxLeft = i
     	rightSum = float("-inf")
     	sum = 0
     	for j in range(mid + 1, high + 1):
        	sum = sum + A[j]
        	if sum > rightSum:
        		rightSum = sum
        		maxRight = j
               
	return(A, maxLeft, maxRight, leftSum + rightSum)
        
'''
Linear algorithm to solve the max subarray problem.
Parameters: 
A - Array to search for maximum subarray from.
Returns:
Maximum subarray sum, start and end positions of maximum subarray.
'''
def Linear_Max_Subarray(A):
    maxSum = maxSoFar = A[0]
    subArrayStart = subArrayEnd = 0
    for i in range(1, len(A)):
        maxSoFar = max(A[i], maxSoFar + A[i])
        if maxSoFar == A[i]:
            subArrayStart = i
        maxSum = max(maxSum, maxSoFar)
        if maxSum == maxSoFar:
            subArrayEnd = i
    return [A, subArrayStart, subArrayEnd, maxSum]

'''
get time data from function with various input sizes
parameters:
functionToCall: function of algorithm you want to test
inputSizes: list of input sizes
Returns - A list of time data for each inputSize
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
        print('n = ' + str(inputSizes[x]) + ': ' + str(timeList[x]))

'''
creates output file
parameters:

function - function of algorithm you want to call
this function should take in a single list of integers, and return a list in the form:
[Full array, Start of subarray, end of subarray, sum of subarray]

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


#-----Similar calls should work for your function as long as the function takes in a single list of integers, and returns a list in the form:
#[Full array, Start of subarray, end of subarray, sum of subarray]
    

'''
These one's should be good for actual experimental data, but they take awhile:
'''
enumInputSizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
betterEnumInputSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]



'''
#shorter tests to try your code on (shouldn't take forever)
enumInputSizes = [50, 100, 150, 200, 250]
betterEnumInputSizes = [100, 200, 300, 400, 500]
'''

#Gets experimental data for various n values for both enum functions
#getExperimentalData(Enum_Max_Subarray, enumInputSizes)
#getExperimentalData(Better_Enum_Max_Subarray, betterEnumInputSizes)



#takes in input file and writes results in specified file -- see note above about functions to pass in
createOutputFile(Enum_Max_Subarray, 'MSS_TestProblems.txt', 'outEnum.txt')
createOutputFile(Better_Enum_Max_Subarray, 'MSS_TestProblems.txt', 'outBE.txt')
createOutputFile(DCHelper, 'MSS_TestProblems.txt', 'outDC.txt')
createOutputFile(Linear_Max_Subarray, 'MSS_TestProblems.txt', 'outLin.txt')




