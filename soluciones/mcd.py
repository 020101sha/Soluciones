"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa que calcula el máximo común divisor (MCD) de dos
números naturales. El MCD de dos números, es el número más grande que
los divide a los dos.
"""
from unittest import main, TestCase


def mcd_recursivo(a: int, b: int) -> int:
    """Calcula el MCD de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCD de los dos números.
    :rtype: int
    """
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)


def mcd_while(a: int, b: int) -> int:
    """Calcula el MCD de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCD de los dos números.
    :rtype: int
    """
    while b != 0:
        a, b = b, a % b
    return a


def mcd_for(a: int, b: int) -> int:
    """Calcula el MCD de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCD de los dos números.
    :rtype: int
    """
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


class Test(TestCase):

    data = (
        ((6, 9), 3),
        ((12, 8), 4),
        ((12, 18), 6),
        ((450, 360), 90),
    )

    def test_functions(self):
        for (a, b), expected in self.data:
            self.assertEqual(mcd_recursivo(a, b), expected)
            self.assertEqual(mcd_while(a, b), expected)
            self.assertEqual(mcd_for(a, b), expected)


if __name__ == '__main__':
    main()