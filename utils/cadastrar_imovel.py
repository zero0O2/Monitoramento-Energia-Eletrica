from dados.dados import imoveis

#apenas testando como funcionalidade o sistema de funcoes externas
def Cadastrar_Imovel():
    newImovel = {
        "id": 3,
        "nome": "Casa Grande na Praia",
        "tipo": "residencial",
        "meta_kwh": 250
    }
    imoveis.append(newImovel)
