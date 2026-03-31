#In this section we'll learn to use IF,ELSE,ELIF and Boolean

# Here's a simple example of an age check

age = int(input("Enter your age: "))

if age >= 18:
print("You are now signed up!")

# Here's an example of the user being rejected for meeting the reuirements using the ELSE statement

age = int(input("Enter your age: ") )

if age >= 18:
. print("You are now signed up!")
else:|
print("You must be 18+ to sign up")

# Here's an example of the user not being born yet trying to sighn up! using the ELIF statement

age = int(input("Enter your age: "))

if age >= 100:
print("You are too old to sign up")
elif age >= 18:
print("You are now signed up!")
elif age < 0:
print("You haven't been born yet!")
else:
print("You must be 18+ to sign up")

# Heres an Example of Boolean as the user is trying to get a discount

is_student = True

if is_student:
    print("You get a student discount!")
else:
    print("You do not get a student discount.")
