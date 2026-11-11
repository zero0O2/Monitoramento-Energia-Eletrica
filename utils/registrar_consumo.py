from dados.dados import imoveis,registros
"""{
    "id_imovel": 1,
    "data": "2026-01",
    "kwh": 180
}"""

def Registrar_Consumo():
    print(f"{'REGISTRAR CONSUMO':-^45}\n")
    while True :
        try:
            id_imovel = int(input("id do imovel: "))
        except Exception:
            print("Erro ao enviar, somente numeros sao permitidos\n")
            continue

        tem_imovel = False
        for imovel in imoveis:
            if imovel["id"] == id_imovel:                
                tem_imovel = True
                break

        if not tem_imovel: 
            print("Imovel não indentificado tente novamente\n")
            continue
        break
    while True:
        data = ""
        try:
            mes = int(input("Mes 1 a 12: "))
            ano = int(input("Ano (ex:1999): "))
            if mes >= 1 and mes <= 12 and len(str(ano)) == 4 and ano > 0 :
                data = f"{ano}-{mes:02}"
                break
            
            print("Data invalida, tente novamente")
        except Exception as e:
            print("Somente numeros permitidos",e)

    data_ja_cadastrada = False
    registro_repetido = {}
    indice_registro_repetido = 0
    for i in range(len(registros)):
        if registros[i]["id_imovel"] == id_imovel and registros[i]["data"] == data:
            data_ja_cadastrada = True
            registro_repetido = registros[i]
            indice_registro_repetido = i

    if data_ja_cadastrada:
        print("A data descrita já tem um registro feito")
        print(f"registro ja feito: {registro_repetido}\n")
        alteracao = input("Deseja continuar e realizar a atualização? ").lower().strip() 

        if alteracao == "n" or alteracao == "nao" or alteracao == "não":
            print(f"\n{'registro cancelado':-^45}")
            return


    while True:
        try:
            kwh = int(input("\nConsumo do mes: "))
            if kwh >= 1:
                break
        except Exception:
            print("Entrada ivalida, tente novamente")

    if data_ja_cadastrada:
        registros[indice_registro_repetido] = {"id":registro_repetido["id"],"id_imovel": id_imovel,"data": data,"kwh": kwh}
    else:
        id_registro = 0
        if len(registros) > 0:
            id_registro = registros[-1]["id"] + 1

        new_registro = {
            "id":id_registro,
            "id_imovel": id_imovel,
            "data": data,
            "kwh": kwh
        }
        registros.append(new_registro)

    print(f"\n{' Registro feito com sucesso ':-^45}\n")

    for registro in registros:
        print(registro)
            