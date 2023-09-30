def insertionSort(arr):
    for i in range(1,len(arr)):
        pos=i
        current_element=arr[i]
        while pos>=1 and arr[pos-1]>current_element:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current_element
data=[1,4,2,5,6,3,5]
insertionSort(data)
print(data)