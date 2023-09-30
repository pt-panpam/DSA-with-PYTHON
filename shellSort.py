def shellSort(arr):
    gap=len(arr)//2
    while gap>0:
        for i in range(gap,len(arr)):
            current_element=arr[i]
            pos=i
            while pos>=gap and current_element<arr[pos-gap]:
                arr[pos]=arr[pos-gap]
                pos=pos-gap
            arr[pos]=current_element
        gap=gap//2
data=[1,43,5,2,6,2]
shellSort(data)
print(data)