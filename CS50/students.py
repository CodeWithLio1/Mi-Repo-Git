# Se inicia la lista
students = []

# Se abre el csv
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        # A student se le asigna la libreria que indica al texto name su valor 
        student = {"name":name, "house":house}
        # Se agrega el estudiante a la listo con ".append(student)"
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
