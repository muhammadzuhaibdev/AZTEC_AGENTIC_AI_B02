# create student app in python,
# default 5 students entities should be there in list by default
# add new student
# show all student's emails and id's
# update any student
# delete any student

studentsData = [
    {
        "id": 1,
        "name": "Zuhaib",
        "email": "zuhaib@gmail.com",
        "age": 25,
    },
    {
        "id": 2,
        "name": "Hamza",
        "email": "hamza@gmail.com",
        "age": 29,
    },
    {
        "id": 3,
        "name": "Abdullah",
        "email": "abdullah@gmail.com",
        "age": 39,
    },
    {
        "id": 4,
        "name": "Ahmad",
        "email": "ahmad@gmail.com",
        "age": 31,
    },
    {
        "id": 5,
        "name": "Hassan",
        "email": "hassan@gmail.com",
        "age": 30,
    },
]

# delete student through while
userInput = int(input("Enter student data ID: "))

i = 0
while i < len(studentsData):
    if studentsData[i]["id"] == userInput:
        studentsData.pop(i)
        print("Student deleted successfully!")
        break
    
print(studentsData)

# Add new student
userName = input("Enter your name: ")
userEmail = input("Enter your email: ")
userAge = input("Enter your age: ")


studentsData.append({
    "id": len(studentsData) + 1,
    "name": userName,
    "email": userEmail,
    "age": userAge
})

print(studentsData)


# Read Data
i = 0
while i < len(studentsData):
    print(studentsData[i]["email"] + " ==> " + str(studentsData[i]["id"]))
    i += 1
