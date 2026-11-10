# Assignment Operator (=, +=, -=, *=, /=, %=, //=, **=)
num1 = 26// 2 % 3 + 10**2
num1 -= 10
print(num1)


num1 += 35
num1 -= 15
num1 *= 2
num1 /= 2
num1 //= 3
num1 %= 2
num1 **= num1


# Comparion Operators (==, !=, < , > , <=, >=)
num1 = 10
num2 = 20

result = num1 % num2 + 20 // 2 <=  True + 1
print(result)

result = num1 + 20 >= num2 - 10
#  < 0 False Values
# <1 True Values 


# Logical Operators (and , or, not)

result = not(10 / num1 + num2 % 3 == 0 and 10 + num2 + num1 % 3 == 1)
result = not(-100)
print(result)

# and Operator
# T and T => T
# T and F => F
# F and T => F
# F and F => F


# or Operator
# T and T => T
# T and F => T
# F and T => T
# F and F => F

# not operator
# not True


# Membership Operator
userName = "Muhammad Zuhaib"
print("Muhammad Zuhaib" not in userName)


# Identity Operator
userName = "Muhammad Zuhaib"
print(userName is not "Muhammad Zuhaib" )