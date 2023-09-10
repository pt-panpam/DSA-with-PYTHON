def largestNum(array):
    largest=float('-inf')
    for i in range(len(array)):
        if largest<array[i]:
            largest=array[i]
    return largest
array=[2,4,5,4,1,8,67,2,3,21,13]
print("largest Number is:",largestNum(array))