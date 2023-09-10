import math
def maxSum(Number,l):
    maxsum=(-math.inf)
    l=len(Number)
    for i in range(len(Number)):
        for j in range(i,len(Number)):
            currentsum=0
            for k in range(i,j+1):
                currentsum=currentsum+Number[k]
                maxsum=max(currentsum,maxsum)
    print("maxSum is:",maxsum)
Number=[-1,2,6,2,5,-1]
maxSum(Number,len(Number))