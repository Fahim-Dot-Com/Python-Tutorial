#Heres a challenge try and make a Yes or No question using the IF statement

response = input("Would you like food? (Y/N): ")

# Example 1

if response == "Y":
print("Have some food!")
else:
print("No food for you!")



# Example 2 

response = input("Would you like food? (Y/N/Maybe): ")

if response == "Y":
    print("Have some food!")
elif response == "Maybe":
    print("Come back when you decide!")
else:
    print("No food for you!")

# Example 3

wants_food = True

if wants_food:
    print("Have some food!")
else:
    print("No food for you!")
