# There are six types of operators in python.

# Arithmetic Operators

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison Operators

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Note: a = 10      # Assignment
# Note: a == 10     # Comparison

# Assignment Operators

a = 10
print(a)

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

# Logical Operators

a = 10
b = 20

print(a > 5 and b > 15)
print(a > 15 or b > 15)
print(not(a > b))

# Membership Operators

name = "Rani"

print("R" in name)
print("z" in name)

print("R" not in name)
print("z" not in name)


# Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a is not c)
