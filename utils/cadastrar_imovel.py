from dados.dados import imoveis

#apenas testando como funcionalidade o sistema de funcoes externas
def Cadastrar_Imovel():
    if len(imoveis) > 0:
        id = imoveis[-1]["id"] + 1
    else: id = 0
    
    nome = input("digite o nome do imovel: ")
    print("1-residencial")
    print("2-comercial")
    print("3-rural")
    print("4-industrial")

    while True:
        tipo = int(input("digite o tipo do imovel: "))

        if tipo == 1:
            tipo = "residencial"
        elif tipo == 2:
            tipo = "comercial"
        elif tipo == 3:
            tipo = "comercial"
        elif tipo == 4:
            tipo = "comercial"
        else: 
            print("escolhe entre as opções de número acima")
            continue
        break

    while True:
        meta_kwh = int(input("digite o quanto você quer em consumo: "))
        if meta_kwh < 0:
            print("insira um valor valido.")
            continue
        break

    newImovel = {
        "id": id,
        'nome': nome,
        "tipo": tipo,
        "meta_kwh": meta_kwh
    }
    imoveis.append(newImovel)
    print(imoveis)
