'''2)WAP to input the percentage and display the division
>=80 → Distinction
>=65 → First Division
>=55 → Second Division
>=40 → Third Division
<40 → Fail'''

def checkPercentage(percentage):
    if percentage>=80:
        print("Distinction")
    elif percentage>=65:
        print("First Division")
    elif percentage>=55:
        print("Second Division")
    elif percentage>=40:
        print("Third Division")
    else:
        print("Fail")


percentage= int(input("enter the percentage: "))
checkPercentage(percentage)
