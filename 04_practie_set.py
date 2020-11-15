# Write a program to store seven fruits in a list entered by the user.
fruit1 = input("Enter fruit 1: ")
fruit2 = input("Enter fruit 2: ")
fruit3 = input("Enter fruit 3: ")
fruit4 = input("Enter fruit 4: ")
fruit5 = input("Enter fruit 5: ")
fruit6 = input("Enter fruit 6: ")
fruit7 = input("Enter fruit 7: ")
myFruit = [fruit1 , fruit2 , fruit3, fruit4 ,fruit5, fruit6, fruit7]
print(myFruit)

# Write a program to accept marks of 6 students and display the in a sorted manner.
marks1 = int(input("Enter marks of first subject: "))
marks2 = int(input("Enter marks of second subject: "))
marks3 = int(input("Enter marks of third subject: "))
marks4 = int(input("Enter marks of fourth subject: "))
marks5 = int(input("Enter marks of fifth subject: "))
marks6 = int(input("Enter marks of sixth subject: "))
myList = [marks1,marks2,marks3,marks4,marks5,marks6]
myList.sort()
print(myList)

# Check that a tuple cannot be changed in python.
t = ("Spandan","Shravan","Divyansh","Shubham","Pulkit")
t[0] = "Navya"
print(t)

# Write a program to sum a list with 4 numbers.
a = [2,4,5,89]
print(a[0]+a[1]+a[2]+a[3])

# Write a program to count the number of zeros in the following tuple:
a = (7,0,8,0,0,9)
b = a.count(0)
print(b)