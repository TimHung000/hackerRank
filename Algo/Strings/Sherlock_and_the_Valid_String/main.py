from collections import defaultdict


def isValid(s):
    charCount = {}
    for c in s:
        charCount[c] = charCount.get(c, 0) + 1
    
    countSummarize = {}
    for char, count in charCount.items():
        countSummarize[count] = countSummarize.get(count, 0) + 1
    
    if len(countSummarize) == 1:
        return 'YES'
    
    countSummarizeKey = list(countSummarize.keys())
    countSummarizeVal = list(countSummarize.values())
    if len(countSummarize) == 2:
        minCount = countSummarizeKey[0]
        maxCount = countSummarizeKey[1]
        if countSummarizeVal[0] > countSummarizeVal[1]:
            minCount = countSummarizeKey[1]
            maxCount = countSummarizeKey[0]
            
        # there is a letter only appear once. e.g. abbcc
        # in this case we can just delete the 'a' 
        if countSummarize[minCount] == 1 and minCount == 1:
            return 'YES'

        if countSummarize[minCount] == 1 and minCount - maxCount == 1:
            return 'YES'
        
    return 'NO'


if __name__ == '__main__':

    s = input()

    result = isValid(s)
    print(result)