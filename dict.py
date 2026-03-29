student = {"name":"Saurav","age":26,"skills":["Python","C++"] }
print (student["name"])
print (student["skills"])

student["city"] = "Kolkata"
student["age"] = 23
del student["city"]

print(student)

for key, value in student.items():
    print(f"{key}:{value}")

def des_studnet(studnet):
    print("---Studnet profle---")
    for key, value in student.items():
         print(f"{key}:{value}")

des_studnet(student)