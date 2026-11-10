from dados.dados import imoveis
"""{
        "id": 3,
        "nome": "Casa Grande na Praia",
        "tipo": "residencial", #especificar o tipo entre os imóveis 1-residencial, 2-comercial, 3-rural ou 4-industrial e fazer na lista
        "meta_kwh": 250
    }"""
#apenas testando como funcionalidade o sistema de funcoes externas
def Cadastrar_Imovel():
    nome = input("digite o nome do imovel:")
    print("1-residencial")
    print("2-comercial")
    print("3-rural")
    print("4-industrial")
    tipo = input("digite o tipo do imovel")
