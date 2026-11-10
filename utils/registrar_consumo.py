from dados.dados import imoveis,registros
"""{
    "id_imovel": 1,
    "mes": "2026-01",
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

    mes = input("Mes 1 a 12: ")
    ano = input("Ano (ex:1999): ")


            
