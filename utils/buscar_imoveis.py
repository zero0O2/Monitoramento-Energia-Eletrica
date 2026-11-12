from dados.dados import imoveis

def Buscar_Imoveis():
    print(f"\n{'Buscar Imoveis':-^45}")

    entradas = {
        "1":"Nome",
        "2":"id",
        "0":"sair"
    }

    print(f"{'Selecione uma das opções': ^45}\n")
    for entrada in entradas:
        print(f"{f'{entrada} 'f'{" "+entradas[entrada]:->20}': ^45}")
    print("")
    while True:
        #Pede a opção de busca pra pessoa
        while True:
            tipo_busca = input("\nSelecione a opção: ")
            if tipo_busca not in entradas:
                print("Entrada invalida,tente novamente")
                continue
            break

        if tipo_busca == "0" :
            print("bye")
            break

        #verificações de entradas
        imoveis_busca = [] # recebe todos os valores indetificados pela pesquisa,pode ter mais de 1 valor

        if tipo_busca == "1": #Buscar por Nome
            pesquisa_nome = input("Digite o nome do imovel: ").lower().strip()
            for imovel in imoveis:
                if pesquisa_nome in imovel["nome"].lower():
                    imoveis_busca.append(imovel)

        if tipo_busca == "2":
            while True:
                try:
                    pesquisa_id = int(input("Digite o id do imovel: "))
                    for imovel in imoveis:
                        if pesquisa_id == imovel["id"]:
                            imoveis_busca.append(imovel)
                            break
                    break
                except Exception:
                    print("id innvalido, tente novamente\n")

        if len(imoveis_busca) == 0:
            print("Nenhum imovel encontrado")
            continue

        #Daqui pra baixo é o resultado de todas verificações (apos tudo ter dado certo)
        print(f"\n{f" Imoveis encontrados - {len(imoveis_busca)} ":-^45}\n")

        print(f"{"id" f"{"nome": >15}" f"{"tipo": >15}" f"{"meta_kwh": >15}"}")
        print("="*50)
        for imovel_busca in imoveis_busca:
            print(f"{imovel_busca["id"]}     {imovel_busca["nome"]}     {imovel_busca["tipo"]}     {imovel_busca["meta_kwh"]}")
            print("-"*50)

    
        