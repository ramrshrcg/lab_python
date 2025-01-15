#10)WAP program to get the largest number from a list.

list=[5,4,7,9,8,6]
length= len(list)
largest= list[0]
for index in list:
    if index>largest:
        largest = index
    
print(largest)