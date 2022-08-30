import pytest
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@pytest.mark.parametrize("entrada, saida",[
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
])

def test_fibonacci(entrada, saida):
    assert fibonacci(entrada) == saida
