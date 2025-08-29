#Programa: PlatilloBasico
#Objetivo: Ilustrar la esencia del concepto de herencia
#          poniendo como ejemplo los diversos menús que
#          ofrece la Tía Aly.
#Autor: Huitzilopochtli
#Fecha: Martes 26 de agosto de 2025

###¿Cómo les muestro la hora en que compran el menú?

#Comenzamos definiendo nuestra clase
class PlatilloBasico: #Encabezado de la clase

#A partir de este momento, definiremos el cuerpo de la clase
    def __init__(self, *params):
        """
        Método constructor que nos permitirá crear platillos básicos.
        A partir de este método se pueden definir diferentes constructores
        :param self: Hace referencia al objeto mismo.
        :param params: Recibe una lista de parámetros para construir
                       diferentes Cafeteras.
        """
        if len(params) == 0: #Constructor por omisión
            self.__verduras = 'Ensalada con Jicama' #Ensalada con Zanahoria.
            self.__leguminosas = 'Frijoles' #También pueden ser lentejas.
            self.__cereales  = 'Arroz Rojo' #También puede ser arroz amarillo.
            self.__tortillas = 3 #Puedes pedir desde 0 tortillas hasta una cantidad n (con n ∈ N)
        elif len(params) == 4: #Aquí tenemos el chance de poder modificar nuestro menú.
            self.__verduras = params[0]
            self.__leguminosas = params[1]
            self.__cereales = params[2]
            self.__tortillas = params[3]

    #Agregaremos métodos getters y setters

    #Vamos con los métodos GETTERS (me permitirán conocer la
    #naturaleza de mis objetos en un momento dado.

    @property
    def verduras(self):
        """
        Método que me ayudará a conocer que tipo de verduras se le está
        sirviendo en su PlatilloBasico.
        :return: Las verduras de su menú.
        :rtype: str
        """
        return self.__verduras

    @property
    def leguminosas(self):
        """
        Método que me ayudará a saber que tipo de leguminosas le estamos
        sirviendo en su PlatilloBasico.
        :return: Las leguminosas de su PlatilloBasico
        :rtype: str
        """
        return self.__leguminosas

    @property
    def cereales(self):
        """
        Método que me permitirá conocer que tipo de cereales le
        estamos sirviendo.
        :return: Los cereales de su PlatilloBasico
        :rtype: str
        """
        return self.__cereales

    @property
    def tortillas(self):
        """
        Método que me permitirá conocer la cantidad de tortillas
        que le estamos dando.
        :return:
        :rtype: int
        """
        return self.__tortillas

    #Ahora vamos con los SETTERS (métodos que nos ayudarán a modificar
    #la naturaleza de mis objetos). Los métodos SETTERS reciben un
    #argumento y no tienen tipo de retorno.

    @verduras.setter
    def verduras(self, verduras):
        """
        Método que me permitriá elegir el tipo de verduras
        que llevará mi PlatilloBasico.
        :param verduras: Las verduras que el desee.
        """
        self.__verduras = verduras

    @leguminosas.setter
    def leguminosas(self, leguminosas):
        """
        Método que me permitirá elegir el tipo de
        leguminosas que llevaré el PlatilloBasico.
        :param leguminosas: Las leguminosas en cuestión.
        """
        self.__leguminosas = leguminosas

    @cereales.setter
    def cereales(self, cereales):
        """
        Método que pemitirá elegir el tipo de cereales
        que llevará el PlatilloBasico.
        :param cereales: El tipo de cereales de su menú.
        """
        self.__cereales = cereales

    @tortillas.setter
    def tortillas(self, tortillas):
        """
        Método que permitirá elegir la cantidad de
        tortillas que llevará su PlatilloBasico.
        :param tortillas: El número de tortillas.
        """
        self.__tortilla = tortillas

    #Vamos con el método str, el cuál nos permitirá imprimir
    #nuestro PlatilloBasico en formato cadena.
    def __str__(self):
        """
        Método para imprimir un PlatilloBasico en formato cadena.
        :return: El PlatilloBasico en formato cadena.
        """
        return "Platillo Básico: Verduras: {} | Leguminosas: {} | " \
               "Cerelaes: {} | Tortillas: {}".format(self.__verduras,
                                                    self.__leguminosas,
                                                    self.__cereales,
                                                    self.__tortillas)
    def __iter__(self):
        """
        Método que devuelve una representación iterable de un objeto. (Lo ve
        como una lista)
        :return: La representación iterable.
        :rtype: iterable
        """
        return iter(["PB", self.__verduras, self.__leguminosas, self.__cereales, self.__tortillas])

    def __llave(self) -> tuple:
        """
        Método privado (sólo se puede ver desde adentro de la clase)p para
        obtener la llave de un objeto PlatilloBasico.
        :return: Una tupla con los atributos del PlatilloBasico.
        :rtype: tuple
        """
        return self.__verduras, self.__leguminosas, self.__cereales, self.__tortillas

    def __hash__(self) -> int:
        """
        Método que internamente llama a la función hash() para obtener el valor
        hash del objeto PlatilloBasico.
        :return: Un valor entero que corresponde al valor hash del objeto PlatilloBasico.
        :rtype: int
        """
        return hash(self.__llave)

    #Método equals para saber si 2 objetos son iguales de acuerdo a sus a
    #atributos
    def __eq__(self, otro) -> bool:
        """
        Método que permite comparar 2 PlatillosBasicos para saber si
        son iguales.
        :param otro: El otro PlatilloBasico a comparar.
        :return: True si son iguales, False en caso contrario
        :rtype: bool
        """
        respuesta = False
        if isinstance(otro, PlatilloBasico):
            respuesta = self.__llave() == otro.__llave()
        return respuesta


#Aquí un método main para poder ir haciendo pruebas de mi programa
if __name__ == "__main__":

    #Creo algunos objetos (para poder jugar con ellos).
    Platillo1 = PlatilloBasico()
    Platillo2 = PlatilloBasico('Calabazas', 'Frijolitos', 'Avena', 4)
    if Platillo1 == Platillo2:
        print("Son iguales.")
    else:
        print("Son diferentes.")
    print(Platillo1)
    print(Platillo2)







