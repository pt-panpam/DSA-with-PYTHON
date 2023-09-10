print('Enter number upto to get fibonacci series')
num=int(input())
a,b=0,1
count=0
if num<=0:
    print('Enter positive Number')
elif num==0:
    print('fibonacci series upto',num,":")
    print(a)
else:
    print('fibonacci series:')
    while count<num: 
        print(a)
        c=a+b
        a=b
        b=c
        count+=1