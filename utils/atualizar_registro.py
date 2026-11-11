from dados.dados import registros,imoveis
def Atualizar_Registro():
    print(f"{'ATUALIZAR REGISTRO':-^48}\n")

    #menuzin

    print(f"{'id': ^12}{'id_imovel': ^12}{'data': ^12}{'kwh': ^12}\n")
    for registro in registros:
        print(f"{registro["id"]: ^12}{registro["id_imovel"]: ^12}{registro["data"]: ^12}{registro["kwh"]: ^12}")
    print("")

    #while pra repetir as perguntas junto com try para captar erro
    # obs o while bom sempre deixar true pra depois de todos os erros quando houver o acerto dar um brack e seguir rumo do codigo
    while True:
        try:
            #a busca por registro especifico pode ficar lenta,com pouco valores nao vai fazer difereca
            id_registro = int(input("Informe o id :"))
            indice_registro = "null"
            for i in range(len(registros)):
                if registros[i]["id"] == id_registro:
                    indice_registro = i
                    break
            if not indice_registro == "null":
                break

            print("nenhum registro enconntrado, tennte novamente")
            
        except Exception:
            print("id so recebe valores numericos\n")

    print(f"\n{registros[indice_registro]}\n")

    while True:
        try :
            new_kwh = int(input("Qual consumo kwh: "))
            #valores negativos nao sao aceitaveis de forma nehuma, ja o 0 (zero) pode aceitar caso realmente o usuario queira
            #sempre em algo de aceitar valores 0 e bom perguntar antes, ja que nao é normal
            if new_kwh < 0:
                print("Valores negativos não sao aceitos")
                continue
            if new_kwh == 0:
                res_cosumo_zero = input("Continuar com consumo 0? ").lower().strip()
                if res_cosumo_zero == "n" or res_cosumo_zero == "nao" or res_cosumo_zero == "não":
                    continue

            registros[indice_registro]["kwh"] = new_kwh

            print(f"\n{registros[indice_registro]}\n")
            print(f"{' atualização concluida com sucesso ':-^48}")
            break
        except Exception:
            print("Kwh so recebe valores numericos")