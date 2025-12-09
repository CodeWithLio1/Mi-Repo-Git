from hola import hola

def test_default():
    assert("Hola, David") == "Hola, David"


# También podemos testear con un bucle, ej:
def test_argument():
    # Para nombres de la lista
    for name in ['Lio','Lean','Mia']:
        # Se afirma que la fución hola(),
        # debe imprimir el nombre
        assert hola(name) == f"Hola, {name}"
