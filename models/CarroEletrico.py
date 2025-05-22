from typing import Self
from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """ Classe que implementa métodos específicos de carros elétricos
    Argumento: Classe pai Veiculos
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, valor_fipe: float, 
            nAssentos: int, nPortas: int, cor: str,
            nivel_bateria: int, tipo_bateria: str, autonomia: int):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe) #Atributos herdados da classe pai Veiculos.
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia 

    def __str__(self):
        """Retorna uma string com as informações do veiculo"""
        infos = super().__str__()
        infos =  f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Nivel de bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos
    
    def calcular_consumo(self, distancia):
        if distancia > 0:
            consumo = distancia * 0,15
            print("O consumo deste veículo elétrico é de:",consumo,"kWh de energia.")
        if distancia < 0:
            raise DistanciaNegativa("Distância inválida!")
        else:
            print("Sem distância percorrida, sem consumo.")

    def recarregar(self, recarga):
        if self.__nivel_bateria == 100:
            print("Bateria carregada!")
        if self.__nivel_bateria + recarga >= 100:
            print("Carregado! O nivel de bateria é: 100%")
        else:
            self.__nivel_bateria + recarga < 100
            novo = self.__nivel_bateria + recarga
            print("Carregado! O nivel de bateria é:", novo,"%") 
