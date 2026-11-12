from dados.dados import registros

def Formatar_Data_input():
    while True:
        try:
            mes_busca = int(input("Mes 1 a 12: "))
            ano_busca = int(input("Ano (ex:1999): "))
            if not mes_busca >= 1 or not mes_busca <= 12 or not len(str(ano_busca)) == 4 or not ano_busca > 0 :
                print("Data invalida, tente novamente")
                continue
            return ano_busca,mes_busca
        except Exception as e:
            print("Somente numeros permitidos",e)

def Buscar_Registros():
    print(f"\n{'Buscar Registros':-^45}")
    entradas = {
        "1":"Todos",
        "2":"Ate uma data",
        "3":"Apos uma data",
        "4":"Entre duas datas",
        "0":"sair"
    }

    print(f"{'Selecione uma das opções': ^45}\n")
    print(f"{'busca feita por id do imovel': ^45}\n")
    for entrada in entradas:
        print(f"{f'{entrada} 'f'{" "+entradas[entrada]:->24}': ^45}")
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

        while True:
            try:
                id_imovel_input =  int(input("id do imovel: "))
                break
            except Exception:
                print("id invalido, tente novamente")
        
        #verificações de entradas
        registros_busca = []

        if tipo_busca == "1":
            for registro in registros:
                if registro["id_imovel"] == id_imovel_input:
                    registros_busca.append(registro)

        if tipo_busca == "2":
            print(f"\n{'-Informe que data a busca termina-': ^45}")

            ano_busca,mes_busca = Formatar_Data_input()

            for registro in registros:
                try:
                    ano_registro = int(registro["data"].split('-')[0])
                    mes_registro = int(registro["data"].split('-')[1])
                except Exception:
                    print("Erro ao capturar ano e mes de registro")

                if registro["id_imovel"] == id_imovel_input and (ano_registro < ano_busca or (ano_registro == ano_busca and mes_registro <= mes_busca)) :
                    registros_busca.append(registro)

        if tipo_busca == "3":
            print(f"\n{'-Informe que data a busca inicia-': ^45}")

            ano_busca,mes_busca = Formatar_Data_input()

            for registro in registros:
                try:
                    ano_registro = int(registro["data"].split('-')[0])
                    mes_registro = int(registro["data"].split('-')[1])
                except Exception:
                    print("Erro ao capturar ano e mes de registro")

                if registro["id_imovel"] == id_imovel_input and (ano_registro > ano_busca or (ano_registro == ano_busca and mes_registro >= mes_busca)) :
                    registros_busca.append(registro)

        if tipo_busca == "4": 
            print(f"\n{'-Informe que data a busca inicia-': ^45}")
            inicia_ano_busca,inicia_mes_busca = Formatar_Data_input()

            print(f"\n{'-Informe que data a busca termina-': ^45}")
            termina_ano_busca,termina_mes_busca = Formatar_Data_input()

            for registro in registros:
                try:
                    ano_registro = int(registro["data"].split('-')[0])
                    mes_registro = int(registro["data"].split('-')[1])
                except Exception:
                    print("Erro ao capturar ano e mes de registro")

                if registro["id_imovel"] == id_imovel_input and (ano_registro > inicia_ano_busca or (ano_registro == inicia_ano_busca and mes_registro >= inicia_mes_busca)) and (ano_registro < termina_ano_busca or (ano_registro == termina_ano_busca and mes_registro <= termina_mes_busca)):
                    registros_busca.append(registro)

        #bloqueia o display de dados se nao haver dados
        if len(registros_busca) == 0:
            print("Nenhum registro encontrado")
            continue

        #Daqui pra baixo é o resultado de todas verificações (apos tudo ter dado certo)
        print(f"\n{f" Registros encontrados - {len(registros_busca)} ":-^45}\n")

        print(f"{"id" f"{"id_imovel": >15}" f"{"data": >15}" f"{"kwh": >15}"}")
        print("="*50)
        for registro_busca in registros_busca:
            print(f"{registro_busca["id"]}     {registro_busca["id_imovel"]}     {registro_busca["data"]}     {registro_busca["kwh"]}")
            print("-"*50)

    
        