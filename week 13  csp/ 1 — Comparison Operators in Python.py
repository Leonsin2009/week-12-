# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5  #True
7 == 2 * 3 + 1  #True
8 != 8  #False
4 <= 2 + 2  #True

# Write 3 examples that result in True and 3 that result in False.

4 >= 4+4-4  #True
8 < 6-2+3   #False
4 == 4  #True
4 >= 6-2+3  #False
5 == 10-5   #True
4 >= 6-2+3-2    #False


# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.

grade = int(input("Enter your score: "))
if grade >= 60: 
    print("You passed the Test!")
else:
    print("You did not pass the test")


# # The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
password = input("Enter your password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is invalid")