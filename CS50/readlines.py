with open ("names.txt", "r") as file:
# rstrip() Es para que la impresion se encargue de todo
    for line in file:
        print("Hello, ", line.rstrip())
