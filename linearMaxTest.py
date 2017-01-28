testArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

def maxSubarray(array):
    maxEndingHere = maxSoFar = array[0]
    maxBegin = maxEnd = 0
    for i in range(1, len(array)):
        print('i is: {}\nvalue of i is: {}\nmaxEndingHere is: {}\nmaxEndingHere + i is: {}'.format(i, array[i], maxEndingHere, maxEndingHere + array[i]))
        maxEndingHere = max(array[i], maxEndingHere + array[i])
        if maxEndingHere == array[i]:
            print('NEW START POINT SHOULD BE {}'.format(i))
            maxBegin = i
        print('maxSoFar is: {}'.format(maxSoFar))
        maxSoFar = max(maxSoFar, maxEndingHere)
        if maxSoFar == maxEndingHere:
            print('NEW END POINT SHOULD BE {}'.format(i))
            maxEnd = i
        print('\n')
    return [maxSoFar, maxBegin, maxEnd, maxEndingHere]

print(maxSubarray(testArray))
