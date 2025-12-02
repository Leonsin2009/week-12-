# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperatue= int(input("What is the weather today:"))
print(temperatue)

if temperatue >= 110:
    print("It is Extremely Hot outside")
elif 109 >= temperatue >= 70:
    print("Its Hot outside")
elif 69 >= temperatue >= 40:
    print("Its warm outisde")
elif 39 >= temperatue >= 11:
    print("Its cold outisde")
elif temperatue <=10:
    print("Its Extremely cold outisde")