#1)WAP to check if an input number is odd or even

def check(number):
    if (number % 2 )== 0:
        print(f"{number} is even")  
    else:
        print(f"{number} is odd")

number = int(input("Enter the number"))
check(number)
