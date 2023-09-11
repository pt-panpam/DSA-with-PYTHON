def trapwater(height):
    n=len(height)
    leftMax=[0]*n
    leftMax[0]=height[0]
    for i in range(1,n):
        leftMax[i]=max(height[i],leftMax[i-1])
    rightMax=[0]*n
    rightMax[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],height[i])
    trappedwater=0
    for i in range(n):
        waterlevel=min(leftMax[i],rightMax[i])
        trappedwater+=waterlevel-height[i]
    return trappedwater
height=[4,2,0,6,3,2,5]
print(trapwater(height))