a=321
rev=0
count=0
while a>0:
    rev=a%10+rev
    a=a//10
    count+=1
print("reverse is:",rev)