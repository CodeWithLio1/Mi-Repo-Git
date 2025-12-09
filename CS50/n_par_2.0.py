import cowsay

def main():
    n = int(input('Ingrese su número :'))
    es_par(n)

def es_par(numero):
    if numero % 2 == 0:
        cowsay.cow('Es un número par')
    else:
        cowsay.trex('No es un número par')

main()
