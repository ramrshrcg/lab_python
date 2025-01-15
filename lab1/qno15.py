#15) Write a Python program to create a person class. Include attributes like name, country and date of
#birth. Implement a method to determine the person's age.

# class person:
#     Name='',
#     country='',
#     DOB='',
    
#     todaysDate= 2025
#     def totalage():
#        return (person.todaysDate-person.DOB)


# person.DOB=(int(input("enter the date of birth  of a person")))


# print(person.totalage())


from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')  # Format: YYYY-MM-DD

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def display_details(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}"

name = input("Enter the person's name: ")
country = input("Enter the country: ")
dob = input("Enter the date of birth (YYYY-MM-DD): ")

person = Person(name, country, dob)

print("\nPerson Details:")
print(person.display_details())
print(f"Age: {person.calculate_age()} years")
