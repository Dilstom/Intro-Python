# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [num for num in range(6)]

# for num in range(1,6):
#     y.append(num)

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [num ** 3 for num in range(10)]

# for num in range(0,10):
#     y.append(num**3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []

for w in a:
    y.append(w.upper())

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
x = input("Enter comma-separated numbers: ").split(',')

y = [int(n) for n in x if int(n) % 2 == 0]

# for n in x:
#     if n%2==0:
#         y.append(n)

print(y)

