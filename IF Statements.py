#In this section youll learn about IF,ELSE,ELIF statements!

#In this example the we are checkiung the age of the user

age = int(input("Enter your age: "))

if age >= 18:
print("You are now signed up!")

# Over here is what would happen if the user is under 18

# if = Do some code only IF some condition is True
age = int(input("Enter your age: "))

if age >= 18:
print("You are now signed up!")
else:
print("You must be 18+ to sign up")

# Heres a funny example of a user not being yet using the else statement!

age = int(input("Enter your age: "))

if age >= 18:
print("You are now signed up!")
elif age < 0:
print("You haven't been born yet!|")
else:
print("You must be 18+ to sign up")
