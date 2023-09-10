def reverse(array):
    start,end=0,len(array)-1
    while start<end:
        array[start],array[end]=array[end],array[start]
        start=start+1
        end=end-1
array=[5,4,8,9,2]
reverse(array)
print("reverse is:",array)