from persona import Persona
from deportista import Deportista

class Futbolista():
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo, añosPracticando,golesMarcados,tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados=goles
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,roja):
        self._tarjetasRojas=roja
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna

    @classmethod
    def getListaFutbolista(clc):
        return clc.listatoFutbolistas

    def setListaFutbolista(clc, listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"