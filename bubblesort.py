def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
data=[23,22,454,7,55]
bubblesort(data)
print('Sorted array is:')
print(data)