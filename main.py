def isPalindrome(stringInQuestion):
    return stringInQuestion == stringInQuestion[::-1]


def largestPalindrome(stringPalindrome):
    strSplit = list(stringPalindrome)
    print(strSplit)
    loopCount = 0
    maxString = strSplit[0]
    maxInt = 1
    while loopCount < len(strSplit): 
        runningIndex = len(strSplit)-loopCount #length of input minus what number your number you are on
        runningIndex2 = 0
        runningString = ""
        while runningIndex > runningIndex2:
            c = runningIndex2 + loopCount
            runningIndex2+=1
            runningString+=strSplit[c]
            if len(runningString) > maxInt:
                if isPalindrome(runningString):
                    maxString = runningString
                    maxInt = len(runningString)
            
        loopCount += 1
    return maxString

print(largestPalindrome("jhdgkjnasdfgkjhsajghkasjdghkladjgmadsvjkkaskkskjsdgkjhdsgakjdhirpuasdfuhsadgiucgnsfghiuxahfgaijgnkjafshgiufghkfjshhjgascmghgghhghhghghhhhadfjhkjhdsmaaaaaaamgiurmomdad"))