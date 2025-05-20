from .Veiculos import Veiculos

class Frota(Veiculos):
    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, valor_fipe: float, tipo: str):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__tipo = tipo

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos =  f"Placa: {self._Veiculos__placa}\n"
        infos += f"Modelo: {self._Veiculos__modelo}\n"
        infos += f"Marca: {self._Veiculos__marca}\n"
        infos += f"Ano: {self._Veiculos__ano}\n"
        infos += f"Cor: {self._Veiculos__cor}\n"
        infos += f"Tipo: {self.__tipo}\n"
        infos += f"Valor Fipe: {self._Veiculos__valor_fipe}\n"
        return infos

Lista_frota = []  # Lista global de veículos

def adicionar_veiculo(placa, modelo, marca, ano, cor, valor_fipe, tipo):
    placavei = input("Qual a placa do carro? ")
    modelovei = input("Qual o modelo do veículo? ")
    marcavei = input("Qual a marca do seu veículo? ")
    anovei = int(input("Qual o ano do veículo? "))  # convertendo para int
    corvei = input("Qual a cor do veículo? ")
    valorvei = float(input("Qual o valor da fipe do veículo? "))  # convertendo para float
    tipovei = input("Qual tipo de veículo? ")
    Lista_frota.append()
