# lambda function = function written in 1 line  using lambda keyword



# lambda parameters:expression


# def double(x):
#     return x * 2


# print(double(5))


double = lambda x: x * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(5,6))

add = lambda x, y, z : x + y + z
print(add(5,6,7))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))

age_check = lambda age: True if age >= 18 else False
print(age_check(12))