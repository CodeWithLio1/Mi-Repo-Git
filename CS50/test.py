def main():
    n = get_number()
    hola(n)


def get_number():
    while True:
        try:
            numero = int(input("Enter your number: "))
            if numero > 0:
                break
        except ValueError:
            print("Please, Enter a valid number")
    return numero


def hola(numero):
    for _ in range(numero):
        print("hola")


main()

