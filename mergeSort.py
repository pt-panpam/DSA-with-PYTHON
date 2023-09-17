def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_arr =arr[:mid]
        right_arr=arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i,j,k=0,0,0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i=i+1
                k=k+1
            else:
                arr[k]=right_arr[j]
                j=j+1
                k=k+1
        while len(left_arr)>i:
            arr[k]=left_arr[i]
            i=i+1
            k=k+1
        while len(right_arr)>j:
            arr[k]=right_arr[j]
            j=j+1
            k=k+1
                
num=int(input("how many elements you want in list:"))
arr=[int(input()) for x in range(num)]
mergeSort(arr)
print("sorted array is:",arr)