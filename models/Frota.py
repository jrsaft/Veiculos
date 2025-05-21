class Frota:
    def __init__(self):
        self.__frota = []

    def adicionarveiculo(self, veiculo):
        self.__frota.append (veiculo)

    def calcular_consumo(self, distancia: float) -> float:
        consumo = distancia/20
        print("O consumo desta moto é de:",consumo,"litros de gasolina.")

    def consumototal(self, distancia):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total
