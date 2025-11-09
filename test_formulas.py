import unittest
import random
from itertools import product
from formulas import *


class TestFormula(unittest.TestCase):
    def test_constructor_variable(self):
        """Prueba que el constructor de Formula funcione para variables."""
        n = random.randint(0, 100)
        x = Formula(n)
        self.assertIsInstance(x, Formula)
        self.assertEqual(x.izquierda, n)
        self.assertIsNone(x.conectivo)
        self.assertIsNone(x.derecha)

    def test_constructor_negacion(self):
        """Prueba que el constructor de Formula funcione para negaciones."""
        n = random.randint(0, 100)
        x = Formula(n)
        negacion = Formula(x, 'N')
        self.assertIsInstance(negacion, Formula)
        self.assertEqual(negacion.izquierda, x)
        self.assertEqual(negacion.conectivo, 'N')
        self.assertIsNone(negacion.derecha)

    def test_constructor_conjuncion(self):
        """Prueba que el constructor de Formula funcione para conjunciones."""
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        conjuncion = Formula(x, 'C', y)
        self.assertIsInstance(conjuncion, Formula)
        self.assertEqual(conjuncion.izquierda, x)
        self.assertEqual(conjuncion.conectivo, 'C')
        self.assertEqual(conjuncion.derecha, y)

    def test_constructor_disyuncion(self):
        """Prueba que el constructor de Formula funcione para disyunciones."""
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        disyuncion = Formula(x, 'D', y)
        self.assertIsInstance(disyuncion, Formula)
        self.assertEqual(disyuncion.izquierda, x)
        self.assertEqual(disyuncion.conectivo, 'D')
        self.assertEqual(disyuncion.derecha, y)

    def test_constructor_implicacion(self):
        """Prueba que el constructor de Formula funcione para implicaciones."""
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        implicacion = Formula(x, 'I', y)
        self.assertIsInstance(implicacion, Formula)
        self.assertEqual(implicacion.izquierda, x)
        self.assertEqual(implicacion.conectivo, 'I')
        self.assertEqual(implicacion.derecha, y)

    def test_constructor_bicondicional(self):
        """Prueba que el constructor de Formula funcione para bicondicionales.
        """
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        bicondicional = Formula(x, 'B', y)
        self.assertIsInstance(bicondicional, Formula)
        self.assertEqual(bicondicional.izquierda, x)
        self.assertEqual(bicondicional.conectivo, 'B')
        self.assertEqual(bicondicional.derecha, y)

    def test_repr_variable(self):
        """Prueba que __repr__ de Formula funcione para variables."""
        n = random.randint(0, 100)
        x = Formula(n)
        self.assertEqual(repr(x), f'x{n}')

    def test_repr_negacion(self):
        """Prueba que __repr__ de Formula funcione para negaciones."""
        n = random.randint(0, 100)
        x = Formula(n)
        f = Formula(x, 'N')
        self.assertEqual(repr(f), f'(¬x{n})')

    def test_repr_conjuncion_disyuncion(self):
        """Prueba que __repr__ de Formula funcione para conjunciones y
        disyunciones.
        """
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        conjuncion = Formula(x, 'C', y)
        disyuncion = Formula(x, 'D', y)
        self.assertEqual(repr(conjuncion), f'(x{n} ∧ x{m})')
        self.assertEqual(repr(disyuncion), f'(x{n} ∨ x{m})')

    def test_repr_implicacion(self):
        """Prueba que __repr__ de Formula funcione para implicaciones."""
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        implicacion = Formula(x, 'I', y)
        self.assertEqual(repr(implicacion), f'(x{n} → x{m})')

    def test_repr_bicondicional(self):
        """Prueba que __repr__ de Formula funcione para bicondicionales."""
        n = random.randint(0, 100)
        m = random.randint(0, 100)
        while m == n:
            m = random.randint(0, 100)
        x = Formula(n)
        y = Formula(m)
        bicondicional = Formula(x, 'B', y)
        self.assertEqual(repr(bicondicional), f'(x{n} ↔ x{m})')

    def test_lista_variables(self):
        """Prueba que lista_variables de Formula funcione para todas las
        formulas.
        """
        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1, 'N')
        f2 = Formula(x2, 'C', x3)
        f3 = Formula(x4, 'C', f1)
        f4 = Formula(f2, 'D', x5)
        f5 = Formula(x5, 'I', x3)
        f6 = Formula(f3, 'I', f4)
        f7 = Formula(f5, 'B', f6)

        self.assertEqual(x1.lista_variables(), [0])
        self.assertEqual(f1.lista_variables(), [0])
        self.assertEqual(f2.lista_variables(), [1, 2])
        self.assertEqual(f3.lista_variables(), [0, 3])
        self.assertEqual(f4.lista_variables(), [1, 2, 4])
        self.assertEqual(f5.lista_variables(), [2, 4])
        self.assertEqual(f6.lista_variables(), [0, 1, 2, 3, 4])
        self.assertEqual(f7.lista_variables(), [0, 1, 2, 3, 4])

    def test_mayor_variable(self):
        """Prueba que el método mayor_variable de Formula funcione para todas
        las formulas.
        """
        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1, 'N')
        f2 = Formula(x2, 'C', x3)
        f3 = Formula(x4, 'D', f1)
        f4 = Formula(f2, 'I', x5)
        f5 = Formula(x5, 'B', x3)

        self.assertEqual(x1.mayor_variable(), 0)
        self.assertEqual(f1.mayor_variable(), 0)
        self.assertEqual(f2.mayor_variable(), 2)
        self.assertEqual(f3.mayor_variable(), 3)
        self.assertEqual(f4.mayor_variable(), 4)
        self.assertEqual(f5.mayor_variable(), 4)

    def test_numero_conectivos(self):
        """Prueba que el método numero_conectivos de Formula funcione para
        todas las fórmulas.
        """
        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1, 'N')
        f2 = Formula(x2, 'C', x3)
        f3 = Formula(x4, 'D', f1)
        f4 = Formula(f2, 'I', f3)
        f5 = Formula(f4, 'B', x5)

        self.assertEqual(x1.numero_conectivos(), 0)
        self.assertEqual(f1.numero_conectivos(), 1)
        self.assertEqual(f2.numero_conectivos(), 1)
        self.assertEqual(f3.numero_conectivos(), 2)
        self.assertEqual(f4.numero_conectivos(), 4)
        self.assertEqual(f5.numero_conectivos(), 5)

    def test_evalua_variable(self):
        """Prueba que el método evalua de Formula funcione para variables."""
        x = Formula(0)
        self.assertEqual(x.evalua([False]), False)
        self.assertEqual(x.evalua([True]), True)

    def test_evalua_negacion(self):
        """Prueba que el método evalua de Formula funcione para la negacion."""
        x = Formula(0)
        f = Formula(x, 'N')
        self.assertEqual(f.evalua([False]), True)
        self.assertEqual(f.evalua([True]), False)

    def test_evalua_conjuncion(self):
        """Prueba que el método evalua de Formula funcione para
        conjunciones.
        """
        x = Formula(False)
        y = Formula(True)
        conjuncion = Formula(x, 'C', y)
        asignaciones = product([False, True], repeat=2)
        for asignacion in asignaciones:
            self.assertEqual(conjuncion.evalua(asignacion),
                             asignacion[False] and asignacion[True])

    def test_evalua_disyuncion(self):
        """Prueba que el método evalua de Formula funcione para
        disyunciones.
        """
        x = Formula(False)
        y = Formula(True)
        disyuncion = Formula(x, 'D', y)
        asignaciones = product([False, True], repeat=2)
        for asignacion in asignaciones:
            self.assertEqual(disyuncion.evalua(asignacion),
                             asignacion[False] or asignacion[True])

    def test_evalua_implicacion(self):
        """Prueba que el método evalua de Formula funcione para
        implicaciones.
        """
        x = Formula(0)
        y = Formula(1)
        implicacion = Formula(x, 'I', y)
        asignaciones = product([False, True], repeat=2)
        for asignacion in asignaciones:
            self.assertEqual(implicacion.evalua(asignacion),
                             not asignacion[False] or asignacion[True])

    def test_evalua_bicondicional(self):
        """Prueba que el método evalua de Formula funcione para
        bicondicionales.
        """
        x = Formula(0)
        y = Formula(1)
        bicondicional = Formula(x, 'B', y)
        asignaciones = product([False, True], repeat=2)
        for asignacion in asignaciones:
            self.assertEqual(bicondicional.evalua(asignacion),
                             (not asignacion[False] or asignacion[True])
                             and (not asignacion[True] or asignacion[False]))

    def test_aplana(self):
        """Prueba que el método aplana de Formula funcione para para todas las
        fórmulas.
        """
        x1 = Formula(1)
        x2 = Formula(2)
        x3 = Formula(3)

        f1 = Formula(x1, 'N')
        f2 = Formula(x1, 'D', x2)
        f3 = Formula(x2, 'C', x3)
        f4 = Formula(f1, 'I', x3)
        f5 = Formula(f2, 'B', f3)
        f6 = Formula(f5, 'N')

        self.assertEqual(x1.aplana(), [x1])
        self.assertEqual(f1.aplana(), [x1, f1])
        self.assertEqual(f2.aplana(), [x1, f2, x2])
        self.assertEqual(f3.aplana(), [x2, f3, x3])
        self.assertEqual(f4.aplana(), [x1, f1, f4, x3])
        self.assertEqual(f5.aplana(), [x1, f2, x2, f5, x2, f3, x3])
        self.assertEqual(f6.aplana(), [x1, f2, x2, f5, x2, f3, x3, f6])

    def test_aplana_sin_variables(self):
        """Prueba que el método aplana_sin_variables de Formula funcione para
        todas las fórmulas.
        """
        x1 = Formula(1)
        x2 = Formula(2)

        f1 = Formula(x1, 'N')
        f2 = Formula(x1, 'D', x2)
        f3 = Formula(f2, 'C', f1)
        f4 = Formula(f2, 'N')
        f5 = Formula(f3, 'I', f4)
        f6 = Formula(f1, 'B', f5)

        self.assertEqual(x1.aplana_sin_variables(), [])
        self.assertEqual(f1.aplana_sin_variables(), [f1])
        self.assertEqual(f2.aplana_sin_variables(), [f2])
        self.assertEqual(f3.aplana_sin_variables(), [f2, f3, f1])
        self.assertEqual(f4.aplana_sin_variables(), [f2, f4])
        self.assertEqual(f5.aplana_sin_variables(), [f2, f3, f1, f5, f2, f4])
        self.assertEqual(f6.aplana_sin_variables(), [f1, f6, f2, f3, f1, f5,
                                                     f2, f4])


if __name__ == "__main__":
    unittest.main()
