nums = [10, 13, 12, 33, 44, 56, 76, 67, 80]


def numsFunc(values):
    if values % 2 == 0:
        return values + 10

output = list(map(numsFunc,nums))
output2 = list(filter(numsFunc,nums))
print("Map:", output)
print("Filter:" , output2)








# userNames = ["Zuhaib", "Hamza", "Ali", "Zain", "Hassan", "Huzaifa"]


# def myFunc(values):
#     return "Mr. " + values

# mapOutput = list(map(myFunc, userNames))
# filterOutput = list(filter(myFunc, userNames))
# print("Filter List: ", filterOutput)
# print("Map List: ", mapOutput)


# newList = []


# for item in userNames:
#     newList.append("Mr. " + item)

# userNames = newList

# print(userNames)
# print(newList)


# cities = ["Faisalabad", "Lahore", "Karachi", "Islamabad", "Queta", "Multan", "Gujrawala"]

# for item in cities:
#     print(item)

# for index,city in enumerate(cities):
#     print(city)


# for city in cities:
#     print(city)
#     if city == "Islamabad":
#         print("City Found", city)
#         break


# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)


# i = 0
# while i < len(cities):
#     print("while loop", cities[i])
#     i += 1


# fruits = ["Apple", "Mango", "Banana"]

# for fruit in fruits:
#     print(fruit)


# i = 1
# while i <= 5:
#     print(f"2 * {i} = {2 * i}")
#     i += 1

# for item in range(1, 6):
#     print(f"2 * {item} = {2 * item}")


# nums = list(range(1, 6))

# print(nums)

# for item in nums :
#     print(item)
