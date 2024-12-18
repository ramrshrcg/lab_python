#6)WAP to calculate the factorial of an input number.

def factorial (num):
    if num==0 or num==1 :
        return 1
    else:
        return num*factorial(num-1)
    
num= int(input("entrt the number: "))
print(f"factorial of{num} is    {factorial(num)}")
