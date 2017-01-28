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
    outFile.write(" ".join(str(x) for x in A) + '\n')
    outFile.write(" ".join(str(A[x]) for x in range(startPos, endPos+1)) + '\n')
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
        elif(maxSum == rightSum)
                     return (maxSum, rightArray)
        elif(maxSum == middleSum):
                     return (maxSum, A[maxLeft:maxRight + 1])
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
get time data from function with various input sizes
parameters:
functionToCall: function of algorithm you want to test
inputSizes: list of input sizes
Returns - A list of time data for each inputSize
'''
def timeFunction(functionToCall, inputSizes):
    timeList = []
    #go through all input Sizes
    for i in inputSizes:
        currLists = []
        #need to make 10 arrays of each inputSize
        for j in range(10):
            a = []
            #append i random integers to a list
            for k in range(i):
                a.append(random.randint(-1000,1000))
            currLists.append(a)
            
        #currLists now holds 10 arrays of size i
        #call and time the function with 10 different arrays for each inputSize
        times = []
        for j in range(10):                          
            startTime = time.time()
            functionToCall(currLists[j])
            times.append(time.time() - startTime)
        avgTime = sum(times) / 10.0
        timeList.append(avgTime) #timeList holds the averages for all
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
        print("n = " + str(inputSizes[x]) + ": " + str(timeList[x]))

'''
creates output file
parameters:

inFilename - string of filename for input
outFilename - string of filename for output
'''
def createOutputFile(inFilename, outFilename):
    outFile = open(outFilename, 'w') #open outFile here so it overwrites existing file only once
    data = getInputData(inFilename)
    params = []
    functionsList = [Enum_Max_Subarray, Better_Enum_Max_Subarray, DCHelper] ##NEED TO ADD LINEAR FUNCTION
    functionNames = ["Enumerative", "Better Enumerative", "Divide and Conquer", "Linear"]
    for i in range(len(functionsList)):
        outFile.write("-------------" + functionNames[i] + "-------------\n\n")
        for j in range(len(data)):
            params = functionsList[i](data[j])
            #parameters for each function should be (outfile, originalArray, startPos, endPos, maximum)
            writeData(outFile, params[0], params[1], params[2], params[3])
    outFile.close()



#-----Similar calls should work for your function as long as the function takes in a single list of integers, and returns a list in the form:
#[Full array, Start of subarray, end of subarray, sum of subarray]
    

enumInputSizes = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
betterEnumInputSizes = [7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000]

#Gets experimental data for various n values for both enum functions
#getExperimentalData(Enum_Max_Subarray, enumInputSizes)
getExperimentalData(Better_Enum_Max_Subarray, betterEnumInputSizes)


''' THE LINE BELOW SHOULD BE THE ONLY LINE WE NEED FOR OUR SUBMISSION -- IT SHOULD HAVE
MSS_Problems.txt as inputFile and MSS_Results.txt as outputFile'''

#takes in input file and writes results in specified file -- see note above about functions to pass in
#createOutputFile('MSS_Problems.txt', 'MSS_Results.txt')






