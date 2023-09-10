def binarySearch(array,key):
    start=0
    end=len(array)-1
    mid=(start+end)//2
    while start<=end:
        if array[mid]==key:
            print("Number is at index:",mid)
        if array[mid]<key:
            start=mid+1
        else:
            end=mid-1
    return -1
array=[12,23,343,565,24,56]
key=565
print("Number is at index",binarySearch(array,key))