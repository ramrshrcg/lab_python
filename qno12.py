'''
12)WAP to find the sum of all items in a dictionary
Input: {'a': 100, 'b':200, 'c':300}
Output: 600
Input: {'x': 25, 'y':18, 'z':45}
Output: 88
'''
dict={
    'a': 100,
    'b':200,
    'c':300
}
sum=0
for i in dict:
    sum+=dict[i]
print(sum)
