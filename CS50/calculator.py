# Calculator

def main():
    x = int(input('Enter your number:'))
    print('What is x?',square(x))

#
def square(n):
    return n*n


# Encapsula el código de arriba,
#esto permite importar modulos a otros arrchivos
if __name__ == '__main__':
    main()

