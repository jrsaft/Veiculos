from .Veiculos import Veiculos

class caminhao(Veiculos):
    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, valor_fipe: float):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos =  f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos
    
    def calcular_consumo(self, distancia: float) -> float:
        consumo = distancia/5
        print("O consumo desse caminhão é de:",consumo,"litros de gasolina.")
