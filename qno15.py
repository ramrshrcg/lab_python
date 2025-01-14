#15) Write a Python program to create a person class. Include attributes like name, country and date of
#birth. Implement a method to determine the person's age.

class person:
    Name='',
    country='',
    DOB='',
    
    todaysDate= 2025
    def totalage():
       return (person.todaysDate-person.DOB)


person.DOB=(int(input("enter the date of birth  of a person")))


print(person.totalage())

