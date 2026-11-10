evenSum = 0
oddSum = 0

i = 1
while i <= 50:
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i     
    
    i += 1
    
print(evenSum)
print(oddSum)



userNames = ["Zuhaib", "Asad", "Ali", "Umar", "Abdullah", "Hassan"]

i = 0
while i < len(userNames):
    userNames[i] = "Mr." + userNames[i]
    i += 1

print(userNames)


userInput = int(input("Enter your table number"))

i = 1
while i <= 10:
    print(f"{userInput} * {i} = {userInput * i}")
    i += 1


i = 1
while i <= 10:
    print("Hello World", i)
    i += 1