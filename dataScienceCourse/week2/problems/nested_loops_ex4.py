num_people = 7
names = []
for i in range(1, num_people + 1):
    name = input("Enter name " + str(i) + ": ")
    names.append(name)

grades = []
for name in names:
    math = float(input("How much did " + name + " get in Mathematics? "))
    eng = float(input("How much did " + name + " get in English? "))
    mfl = float(input("How much did " + name + " get in MFL? "))
    person_grade = [math, eng, mfl]
    grades.append(person_grade)

print("----------------")
print("Mathematics grades: ")
for i in range(0, num_people):
    print(names[i] + ": " + str(grades[i][0]))

print("----------------")
print("English grades: ")
for i in range(0, num_people):
    print(names[i] + ": " + str(grades[i][1]))

print("----------------")
print("MFL grades: ")
for i in range(0, num_people):
    print(names[i] + ": " + str(grades[i][2]))
