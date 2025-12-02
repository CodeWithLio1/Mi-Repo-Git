from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

#
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

#
def test_zero():
    assert square(0) == 0


# También podemos testear con un bucle, ej:
def test_argument():
    # Para nombre en el rango de la lista
    for name in range ['Lio','Lean','Mia']:
        # Se afirma que la fnción hola(),
        # debe imprimir el nombre
        assert hello(name) f'Hello,{name}'
