array=[1,4,5,3,2]
for i in range(len(array)-1):
    minPose=i
    for j in range(i+1,len(array)):
        if array[minPose]>array[j]:
            minPose=j
    array[minPose],array[i]=array[i],array[minPose]
print(array)
# def printt(array):
#     for i in range(len(array)):
#         print(array[i],end=" ")
# printt(array)
