def update(marks):
    for i in range(len(marks)):
        marks[i] = marks[i] + 1

marks = [3, 5, 6]
update(marks)
for i in range(len(marks)):
    print(marks[i], end=" ")
print()
