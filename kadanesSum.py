import math
def kadanas(num,l):
    l=len(num)
    maxsum=-math.inf
    currSum=0
    for i in range(0,l):
        currSum=currSum+num[i]
        if currSum<0:
            currSum=0
        maxsum=max(currSum,maxsum)
    print("Our max sub array is:",maxsum)
num=[-1,2,6,2,5,-1]
kadanas(num,len(num))
    