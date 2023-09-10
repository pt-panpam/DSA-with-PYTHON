print('Enter Number to count even Odd')
a=int(input())
evenCount=0
oddCount=0
while a>0:
    rem=a%10
    if rem%2==0:
      evenCount=evenCount+1
    else:
        oddCount=oddCount+1
    a=a//10
print("No. of even digit is:",evenCount,"No. of odd digit is:",oddCount)