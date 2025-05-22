class Frota:
    def __init__(self):
        self.__frota = []

    def adicionarveiculo(self, veiculo):
        self.__frota.append (veiculo)

    def mostrarveiculos(self):
        print(self.__frota)

    def calcular_consumo(self, distancia: float) -> float:
        if distancia > 0:
            consumo = distancia/20
            print("O consumo deste veículo é de:",consumo,"litros de gasolina.")
        elif distancia < 0:
            print("Distância inválida!")
        else:
            print("Sem distância percorrida, sem consumo.")

    def consumototal(self, distancia):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total
