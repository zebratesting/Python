students={"john":["python","selenium","aptitude"],"David":["python","ReactJs"]}

print(type(students))
keys=students.keys()

for eachkey in keys:
    print(eachkey, "taken courses are:")
    for eachcourse in students[eachkey]:
        print(eachcourse)