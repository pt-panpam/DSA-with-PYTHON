def pair(array):
    for i in range(len(array)):
        curr=array[i]
        for j in range(i+1,len(array)):
            print("(",curr,",",array[j],")")
array=[1,2,3,4,5]
pair(array)