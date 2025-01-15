#5)WAP to enter the marks of 10 students and display it.
noOfStudent=10
marks=[]
for i in range(noOfStudent):
    mark= int(input(f"marks of {i+1} student  "))
    marks.append(mark)
print(marks)


for mark in range(noOfStudent):
    print(f"the mark of {mark+1} student is {marks[mark]}")
