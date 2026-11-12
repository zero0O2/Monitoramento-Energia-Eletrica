from dados.dados import imoveis, registros

def Alertas():
    for imovel in imoveis:
        registro_do_imovel = []
        
        for registro in registros:
            if registro["id_imovel"] == imovel["id"]:
                registro_do_imovel.append(registro)

        print("")
        print(f"{f"{imovel["nome"]} - meta {imovel['meta_kwh']}": ^45}")

        for registro in registro_do_imovel:
            print(registro)
            if registro["kwh"] > imovel["meta_kwh"]:
                limite_excedido = int(registro["kwh"]/imovel["meta_kwh"]*100) - 100
                print(f"Registro esta {int(limite_excedido)}% acima do limite\n")
            else:
                print(f"Registro nos padrões\n")