print('enter number to get sum:')
num=int(input())
sum=0
while num>0:
    sum=num%10+sum
    num=num//10
print('sum of digit is:',sum)