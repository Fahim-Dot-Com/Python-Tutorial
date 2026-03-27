# typecasting = The process of converting a value of one data type to another.
# (string, integer, float, boolean)
# Explicit vs Implicit

# Explicit typecasting is manually converting a value from one data type functions like int(), float(), etc.

name = "Bro"
age = 21
gpa = 1.9
student = True

# typecasting demo

name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

print("\n--- Explicit Typecasting Examples ---")

# int → float
age_float = float(age)
print(age_float)
print(type(age_float))

# float → int
gpa_int = int(gpa)
print(gpa_int)
print(type(gpa_int))

# bool → string
student_str = str(student)
print(student_str)
print(type(student_str))

# Implicit typecasting is automatically converting a value from another data type to another during an operation without the you telling it.

print("\n--- Implicit Typecasting Examples ---")

# int → float (automatic)
result = age + gpa   # age becomes float automatically
print(result)
print(type(result))  # float

# bool → int (True = 1, False = 0)
score = age + student
print(score)
print(type(score))

# bool → float
value = gpa + student
print(value)
print(type(value))
