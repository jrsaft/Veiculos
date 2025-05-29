import re

def validar_cpf(cpf):
    if len(cpf) != 11: #Confere se tem os 11 caracteres que formam o cpf.
        return False
    else:
        padrao = r'^[0-9.,]{3,4}+[0-9.,]{3,4}+[0-9.,]{3,4}+[-0-9.,]{2,3}$' #Padrão para aceitar todas as possibilidades de CPFs.
        return bool(re.match(padrao, cpf)) #return boll para válido e inválido. match para checkar o padrão.

cpfs = ['987,088,900-08', '76549876545'] # Criando os cpfs;

for cpf in cpfs:
    print(f"{cpf}: {'Válido' if validar_cpf(cpf) else 'Inválido'}") #If verdadeiro=Válido // falso=Inválido