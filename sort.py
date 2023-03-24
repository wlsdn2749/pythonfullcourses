# sort() = used with lists
# sort() function = used with iterables


# students = ["Squidaward", "sandy", "patrick", "spongebob", "mr.karbs"]
# students_tuple = ("Squidaward", "sandy", "patrick", "spongebob", "mr.karbs")

# students.sort(reverse=True) # method

# sorted_students = sorted(students, reverse=True)


# for i in students:
#     print(i)

# for i in sorted_students:
#     print(i)



students = (("Squidward", "F", 60),
           ("Sandy", "A", 33),
           ("Patrick", "D", 36),
           ("Spongebob", "B", 20),
           ("Mr.Krabs", "C", 78))

# grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students.sort(key=age)
sorted_student = sorted(students, key=age)
# students.sort(key=age, reverse=True)

for i in sorted_student:
    print(i)