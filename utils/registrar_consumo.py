from dados.dados import imoveis,registros
"""
medelo de imovel
{
    "id":0
    "id_imovel": 1,
    "data": "2026-01",
    "kwh": 180
}
"""

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

            # mes de 1 a 12 (ao guardar a mes na data é feito a formatacao pra ser 2 valores caso so tenha um numero adiciona 0 - :02)
            # data ta vindo como ano-mes (todas tem q vim assim)
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
            if kwh < 0:
                print("Valores negativos não sao aceitos")
                continue
            if kwh == 0:
                res_cosumo_zero = input("Continuar com consumo 0? ").lower().strip()
                if res_cosumo_zero == "n" or res_cosumo_zero == "nao" or res_cosumo_zero == "não":
                    continue
            break
        except Exception:
            print("Entrada ivalida, tente novamente")

    #aqui é a verificaçao final se a data ja foi cadastrada antes entao ela tem um lugar especifico no nosso "banco" entao so troca o valor na mesma posicao
    #se nunca tiver existido nenhum cadastrado na data so segue o rumo ormal de criacao do registro em um dic new_registro
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

    #dando um display em todos os registros pra conseguir ver oq foi feito, resolvi deixar ai
    for registro in registros:
        print(registro)
            