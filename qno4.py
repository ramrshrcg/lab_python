'''#4)WAP to display prime numbers from 1 to 100
def prime(num1, num2):
    for i in range(num1, num2):
        if isprime(i):
            print(i)

def isprime(num):
    for i in range (2, num-1):
        if num % i == 0:
            return False
        return True
prime(1,100)


'''

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) ):
        if num % i == 0:
            return False
    return True
list =[]
print("Prime number from 1 to 100 are:")
for number in range(1, 100):
    if isprime(number):
        list.append(number)

print(list)
