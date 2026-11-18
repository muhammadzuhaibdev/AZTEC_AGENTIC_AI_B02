# variable problem
model = "SKL-4567"
year = 2024
color = "black"
make = "sonata"

# [] => List
# {} => dictionary
# () => functions

# list problem
cars = [
    ["sonata", "SKL-7689", 2025, "black"],
    ["toyota", "TCL-57689", 2020, "white"],
    ["fortuner", "HXL-2024", 2024, "black"],
]

# dictionary
car1 = {
    "make": "sonata",
    "model": "TKL-6578",
    "year": 2024,
    "color": "black",
    "isEngineStarted": True,
}

# create
car1["country"] = input("Entet Country Name: ")

# # read
car1["color"]

# # update
car1["year"] = 2026

# # delete
del car1["isEngineStarted"]

print(car1)


# # CRUD
# # c => create
# # r => read / get
# # u => update
# # d => delete


studentsData = [
    {
        "name": "Ibrahim",
        "email": "ibrahim@gmail.com",
        "age": 25,
        "subject": "BSCS",
    },
    {
        "name": "Zuhaib",
        "email": "zuhaib@gmail.com",
        "age": 26,
        "subject": "BSSE",
    },
    {
        "name": "Hassan",
        "email": "hassan@gmail.com",
        "age": 21,
        "subject": "BSSE",
    },
]

print(studentsData[2]["subject"])


listOfPosts = [
    {
        "id": 9876,
        "title": "My post",
        "caption": "My caption",
        "user": "Muhammad Zuhaib",
    },
    {"id": 9876, "title": "My post", "caption": "My caption", "user": "Hamza"},
    {"id": 9876, "title": "My post", "caption": "My caption", "user": "Abdullah"},
]

listOfPosts[0]["title"] = "My updated post"

print(listOfPosts)