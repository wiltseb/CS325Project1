'''
It's..... a start?

'''
def DandC_Max_Subarray(A, outFile, startPos, endPos):
    if endPos - startPos == 0:
        return [A[startPos], startPos, endPos]
    mid = (startPos + endPos) / 2
    lMax = DandC_Max_Subarray(A, outFile, startPos, mid)
    rMax = DandC_Max_Subarray(A, outFile, mid+1, endPos)
    maxPref = DandC_Max_Prefix(A, startPos, endPos)
    maxSuff = DandC_Max_Suffix(A, startPos, endPos)
    midMax = [maxPref[0] + maxSuff[0], maxPref[2], maxSuff[1]]
    total = 0
    for i in range(startPos, endPos + 1):
        total += A[i]
    current = [total, startPos, endPos]
    maxLRMC = [lMax, rMax, midMax, current]
    t = maxLRMC[0][0]
    p = None
    print maxLRMC
    for m in maxLRMC:
        print m
        if m[0] > t:
            t = m[0]
            p = m
    return p
    
'''
    if lMax[0] > rMax[0]:
        if lMax[0] > current[0]:
            return lMax
    else:
        if rMax[0] > current[0]:
            return rMax
    return current
'''
def DandC_Max_Prefix(A, startPos, endPos):
    if startPos == endPos:
        return [A[startPos], startPos, endPos]
    maximum = A[startPos]
                
    total = 0
    tArray = []
    pos = 0
    for i in range(startPos, endPos+1):
        total += A[i]
        tArray.append(total)
    for i in range(len(tArray)):
        if tArray[i] > maximum:
            maximum = tArray[i]
            pos = i + startPos
    return [maximum, startPos, pos]

def DandC_Max_Suffix(A, startPos, endPos):
    if startPos == endPos:
        return [A[startPos], startPos, endPos]
    maximum = A[endPos]
    total = 0
    tArray = []
    pos = 0
    for i in reversed(range(startPos, endPos+1)):
        total += A[i]
        tArray.append(total)
    for i in range(len(tArray)):
        if tArray[i] > maximum:
            maximum = tArray[i]
            pos = i
    return [maximum, pos, endPos]
