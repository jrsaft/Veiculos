from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletr import CarroConvEletr

voyage = Veiculos("BCE9D36", "Voyage",  "Volkswagen", 
                  2018,    "Vermelho", 47793) #Classe: Veiculos

jetta_gli = CarrosCombustao("JDM9D36", "Jetta GLI",  "Volkswagen", 
                            2025, "Vermelho", 250000, "Gasolina", 
                            4, 5, 2000, "AT 7", 24) #Classe: CarroCombustao

tesla_model = CarroEletrico("IJI8K0T","Tesla model 5","Tesla", 2025, 500000, 5, 4, "Branco",
                            65,"Lítio", 491) #Classe: CarroEletrico

fusca_eletrico = CarroConvEletr(placa="IAA0D40", modelo="Fusca 1600 Elétrico", marca="Volkswagem",
                                ano=1975, cor="Azul", valor_fipe=20000,combustivel= "Gasolina", 
                                nPortas=4, nAssentos= 5, nCilindrada= 1600,nCambio= "MT 4", 
                                nivel_combustivel= 24, nivel_bateria=65, tipo_bateria="Litio", autonomia=150 ) #Classe: CarroConvEletr



print(jetta_gli)
if jetta_gli.abastecer(10):
    print("Abastecido com sucesso!")
else:
    print("Erro ao abastecer")

print(jetta_gli)
print(fusca_eletrico)
