# Se Inicializa una lista
students = []

# Abrimos el archivo .csv 
with open("students.csv") as file:
    # Para las lineas en file
    for line in file:
        # Esta linea almacenamos primer valor antes de la "," en su variable (nombre)
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)


for student in students:
    print(f"{student['name']} is in {student['house']}")
