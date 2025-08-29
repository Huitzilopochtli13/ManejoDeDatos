#Programa: PlatilloConGuisados
#Objetivo: Ilustrar la esencia del concepto de herencia
#          poniendo como ejemplo los diversos menús que
#          ofrece la Tía Aly. Este platillo será más
#          "especializado".
#Autor: Huitzilopochtli
#Fecha: Martes 26 de agosto de 2025

# Como vamos a heredar aspectos del PlatilloBasico, debemos llamar(traer) a
# a dicha clase.
from PlatilloBasico import PlatilloBasico

#Encabezado de la clase.
class PlatilloConGuisados(PlatilloBasico):
    def __init__(self, verduras: str, leguminosas: str, cereales: str,
                 tortillas: str, guisados: int, agua: bool):
        """
        Método constructor que heredará atributos de la clase PlatilloBasico.
        Además, tendrá atributos extras (guisados y agua)
        :param str verduras: nombre de la verdura
        :param str leguminosas: nombre de la leguminosa
        :param str cereales: nombre de la cereal
        :param int tortillas: cantidad de tortillas
        :param int guisados: cantidad de guisados
        :param boolean agua: si llevará agua o no
        """
        super().__init__(verduras, leguminosas, cereales, tortillas)
        self.__guisados = guisados
        self.__agua = agua

    #Comenzamos con los métodos GETTERS.
    @property
    def guisados(self):
        """
        Método que me permitirá conocer el tipo de guisado del PlatilloConGuisados.
        :return: El guisado del platillo
        """
        return self.__guisados

    @property
    def agua(self):
        """
        Método que me permitirá conocer el tipo de agua del PlatilloConGuisados.
        :return: El agua del platillo
        """
        return self.__agua

    #Ahora vamos con los métodos SETTERS. Recuerda que no tienen tipo de retorno.
    @guisados.setter
    def guisados(self, guisados):
        """
        Método que me permitirá modificar el tipo de guisado del PlatilloConGuisados.
        :param guisados: El guisado del platillo.
        """
        self.__guisados = guisados

    @agua.setter
    def agua(self, agua):
        """
        Método que me permitirá modificar el tipo de agua del PlatilloConGuisados.
        :param agua: EL tipo de agua de mi platillo.
        """
        self.__agua = agua

    def __str__(self):
        """
        Metodo para imprimir un PlatilloConGuisado en formato cadena.
        :return: El PlatilloConGuisado en formato cadena.
        :rtype: str
        """
        return super().__str__() + \
            " | Guisado/s: {} | Agua: {}".format(self.__guisados,
                                                 self.__agua)


    def __iter__(self):
        """
        Metodo que devuelve una representación iterable del objeto.
        :return: La representación iterable del PlatilloConGuisado.
        :rtype: iterable (objeto de tipo iterable, es decir, una lista. ¿Qué es iterar? Es repetir
        """
        return iter(["CG", super().verduras, super().leguminosas,
                     super().cereales, super().tortillas, self.__guisados, self.__agua])

    def __llave(self) -> tuple:
        """
        Metodo privado para obtener la llave de un objeto PlatilloConGuisado
        :return: Una tupla con los atributos del PlatilloConGuisado
        :rtype: tuple
        """
        return (super().verduras, super().leguminosas, super().cereales, super().tortillas,
                self.__guisados, self.__agua)

    def __hash__(self) -> int:
        """
        Metodo que internamente llama la función hash() para obtener el valor
        hash del objeto PlatilloConGuisado. (Es como una clave de identificación).
        :return: Un valor entero que corresponde al valor hash del objeto.
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Metodo que permite comparar dos PlatilloConGuisado para saber si son iguales.
        :param otro: El otro PlatilloConGuisado para comparar.
        :return: True si son iguales, False en caso contrario.
        :rtype: bool
        """
        respuesta = False
        if isinstance(otro, PlatilloConGuisados):
            respuesta = self.__llave() == otro.__llave()
        return respuesta

if __name__ == "__main__":
    pcg1 = PlatilloConGuisados("Ensalada con cacahuates", "Frijoles",
                               "Arroz", 2, "Suadero", "Jamaica")
    pcg2 = PlatilloConGuisados("Ensalada con cacahuates", "Frijoles",
                               "Arroz", 2, "Suadero", "Jamaica")
    pcg3 = PlatilloConGuisados("Ensalada con Jicama", "Habas",
                               "Avena", 4, "Tortita de Papa", "Horchata")

    #Imprimiré mis objetos
    print(pcg1)
    print(pcg2)
    print(pcg3)

    #Compararé mis objetos.
    if pcg1 == pcg2:
        print("Son los mismos platillos.")
    else:
        print("No son los mismos platillos.")

    #Otra comparación
    if pcg1 == pcg3:
        print("Son los mismos platillos.")
    else:
        print("No son los mismos platillos.")

    #Estas últimas pruebas las hago para ver si todo va bien hasta el momento.





