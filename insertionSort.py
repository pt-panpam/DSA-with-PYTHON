def insertionSort(arr):
    for i in range(1,len(arr)):
        current_element=arr[i]
        pos=i
        while pos>0 and current_element<arr[pos-1]:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current_element
arr=[2,4,3,5,1]
insertionSort(arr)
print(arr)