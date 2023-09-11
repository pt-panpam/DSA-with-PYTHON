def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
def printt(array):
    for i in range(len(array)):
        print(array[i],end=" ")
array=[2,4,3,1,5]
bubblesort(array)
printt(array)

      #2nd Approach

# array=[2,4,5,3,1]
# for i in range(len(array)-1):
#     for j in range(len(array)-i-1):
#         if array[j]>array[j+1]:
#             array[j],array[j+1]=array[j+1],array[j]
# print(array)
