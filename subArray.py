def subarray(number):
    for i in range(len(number)):
        for j in range(i,len(number)):
            for k in range(i,j):
                print(number[k],end=" ")
            print()
number=[1,2,3,4,5]
subarray(number)