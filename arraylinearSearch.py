def linearSearch(fruits,key):
    for i in range(len(fruits)):
        if fruits[i]==key:
            return i
    return -1
# array=[12,23,34,46,10]
# key=12
fruits=["banana","apple","guavava","mango","orange"]
key="grapes"
index=linearSearch(fruits,key)
if index==-1:
    print ("number not found:")
else:
    print("number at index:",index)
    