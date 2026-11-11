from dados.dados import registros,imoveis
def Atualizar_Registro():
    print(f"{'ATUALIZAR REGISTRO':-^48}\n")

    print(f"{'id': ^12}{'id_imovel': ^12}{'data': ^12}{'kwh': ^12}\n")
    for registro in registros:
        print(f"{registro["id"]: ^12}{registro["id_imovel"]: ^12}{registro["data"]: ^12}{registro["kwh"]: ^12}")
    print("")

    while True:
        try:
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