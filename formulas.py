 #Universidad Nacional Autónoma de México
 #Facultad de Ciencias
 #Licenciatura en Ciencias de la Computación
 #Estructuras Discretas 
 #Practica6
 #Escrito por: Hernandez Vazquez Diego y Bruno Bernardo Soto Lugo

from typing import List

Asignacion = List[bool]


class Formula:
    """Clase para representar fórmulas booleanas."""
    def __init__(self, izquierda, conectivo=None, derecha=None):
        """Constructor para la clase. En el caso de las variables, izquierda es
        el identificador de la variable, el cual debe ser un entero, y los
        demás argumentos deben ser None. El atributo conectivo debe ser un
        string, 'C'(onjunción), 'D'(isyunción), 'I'(mplicación), 'N'(egación) o
        'B'(icondicional). Para cualquier fórmula que no sea una variable, el
        atributo izquierda debe ser una fórmula, y para las fórmulas con
        conectivo distinto a 'N', el atributo derecho también tiene que ser una
        fórmula.
        """
        conectivos = ['C', 'D', 'I', 'B', 'N']

        # variables
        if conectivo is None:
            if not isinstance(izquierda, int) and izquierda < 0:
                raise TypeError("Las variables deben ser números naturales.")
            # fórmulas
        else:
            if conectivo not in conectivos:
                raise ValueError(f"El conectivo {conectivo} es incorrecto.")
            if not isinstance(izquierda, Formula):
                raise TypeError(f"{izquierda} no es de tipo fórmula.")
            # negación unaria
            if conectivo == 'N' and derecha is not None:
                raise TypeError(
                    "No debe existir fórmula derecha en la negación."
                )
            # conectivos binarios
            if conectivo != 'N' and not isinstance(derecha, Formula):
                raise TypeError(f"{derecha} no es de tipo fórmula.")
        self.izquierda = izquierda
        self.conectivo = conectivo
        self.derecha = derecha

    def __repr__(self):
        """Representación en cadena, legible para humanos, de las fórmulas."""
        return ""

    def lista_variables(self):
        """Devuelve la lista de todas las variables de una fórmula en orden.
         Si la fórmula es una variable, regreso una lista con ese número.
         Si es una negación, regreso la lista de la subfórmula
         Si es un conectivo binario, obtengo las listas de izquierda y derecha y las mezclo con merge ascendente y evita duplicados.
        """
        def merge(a: List[int], b: List[int]) -> List[int]:
            # si alguna está vacía, regreso el caso base
            if not a:
                return b[:]
            if not b:
                return a[:]
            # comparo las cabezas
            if a[0] == b[0]:
                # si son iguales, incluyo una sola vez y avanzo en ambas
                return [a[0]] + merge(a[1:], b[1:])
            elif a[0] < b[0]:
                return [a[0]] + merge(a[1:], b)
            else:  # b[0] < a[0]
                return [b[0]] + merge(a, b[1:])

        # Caso hoja: variable
        if self.conectivo is None:
            return [self.izquierda]

        # Caso negación: solo la subfórmula izquierda
        if self.conectivo == 'N':
            return self.izquierda.lista_variables()

        # Caso binario: obtengo listas de ambas ramas y las mezclo
        izquierda_vars = self.izquierda.lista_variables()
        derecha_vars = self.derecha.lista_variables()
        return merge(izquierda_vars, derecha_vars)

    def mayor_variable(self):
        """
        Devuelve la variable de mayor número que aparece en la fórmula.
        - Si la fórmula es una variable, regreso ese número.
        - Si la fórmula es una negación, solo reviso la parte izquierda.
        - Si la fórmula tiene dos lados, comparo recursivamente ambos lados.
        """
        # Caso 1: la fórmula es una variable
        if self.conectivo is None:
            return self.izquierda
        # Caso 2: negación del lado izquierdo
        if self.conectivo == 'N':
            return self.izquierda.mayor_variable()
        # Caso 3: busco la mayor variable de cada lado recursivamente
        mayor_izq = self.izquierda.mayor_variable()
        mayor_der = self.derecha.mayor_variable()
        # Comparo las dos 
        if mayor_izq >= mayor_der:
            return mayor_izq
        else:
            return mayor_der

    def numero_conectivos(self):
        """Devuelve el número de conectivos que ocurren en la fórmula.
        - Si la fórmula es una variable, no hay conectivos -> 0.
        - Si la fórmula es una negación, cuento 1 por la negación y llamo recursivamente a la parte izquierda.
        - Si la fórmula tiene un conectivo binario, cuento 1 por ese conectivo y llamo recursivamente a izquierda y derecha y sumo los resultados.
        """
        # Caso variable:
        if self.conectivo is None:
            return 0
        # Caso negación:
        if self.conectivo == 'N':
            # cuento 1 por la negación y sumo lo que devuelva 
            return 1 + self.izquierda.numero_conectivos()
        # Caso binario:
        return 1 + self.izquierda.numero_conectivos() + self.derecha.numero_conectivos()

    def _evalua_aux(self, asignacion: Asignacion, posiciones: List[int]):
        """Función auxiliar para evaluar una fórmula. Recibe una lista de
        booleanos (una asignación de verdad), y una lista con los números de
        las variables correspondientes.
        Eg. _evalua_aux([False, True, True], [1, 2, 5]) corresponde a:
        x1 = False
        x2 = True
        x5 = True
        """
        return False

    def evalua(self, asignacion: Asignacion):
        """Devuelve el valor de verdad de la fórmula bajo una asignación dada,
        que recibe como entrada en la forma de una lista de booleanos.
        """
        return False

    def aplana(self):
        """Devuelve una lista con la versión aplanada (inorden) del árbol de
        sintáxis de la fórmula.
        - Si la fórmula es una variable, regreso una lista con ella misma.
        - Si es una negación, primero aplano la subfórmula izquierda y luego pongo la negación (la raíz) al final.
        - Si es un conectivo binario, aplano izquierda, pongo la raíz, y luego aplano derecha; todo concatenado. 
        """
        # Caso base: Una hoja
        if self.conectivo is None:
            return [self]
        # Caso negación 
        if self.conectivo == 'N':
            return self.izquierda.aplana() + [self]
        # Caso binario:
        return self.izquierda.aplana() + [self] + self.derecha.aplana()


    def aplana_sin_variables(self):
        """Devuelve una lista con la versión aplananada del árbol de sintaxis de la fórmula, sin las hojas.
        - Si la fórmula es una variable hoja, devuelvo [] porque no quiero variables.
        - Si la fórmula es una negación, primero aplanamos la subfórmula izquierda  y luego añadimos la negación. 
        - Si la fórmula es un conectivo binario, aplanamos izquierda, luego
          añadimos la raíz y luego aplanamos derecha.
        - Hago concatenaciones de listas manualmente porque quiero practicar recursión y ver paso a paso cómo se arma la lista final.
        """
        # Caso base: Una hoja
        if self.conectivo is None:
            return []

        # Caso negación: aplanar izquierda y añadir la negación
        if self.conectivo == 'N':
            return self.izquierda.aplana_sin_variables() + [self]

        # Caso binario:  aplanar izquierda, añadir la raíz y aplanar derecha
        return self.izquierda.aplana_sin_variables() + [self] + self.derecha.aplana_sin_variables()
