from dados.dados import imoveis,registros
from func.calcular_custo_kwh import Calcular_Custo_Kwh


def Economia_Potencial():
    print(f"{'= Economia Potencial =':-^45}")

    imoveis_potencial = []

    for imovel in imoveis:
        registros_imovel = []
        soma_registros_kwh = 0
        for registro in registros:
            if registro["id_imovel"] == imovel["id"] :
                registros_imovel.append(registro)
                soma_registros_kwh += registro["kwh"]

        media_kwh = float(soma_registros_kwh/len(registros_imovel))

        if media_kwh <= imovel["meta_kwh"]:
            porcentagem_economica = (imovel["meta_kwh"]-media_kwh)/imovel["meta_kwh"]*100
            imoveis_potencial.append([imovel,media_kwh,porcentagem_economica])

            if len(imoveis_potencial) > 1 and imoveis_potencial[-1][2] > imoveis_potencial[-2][2]:
                imoveis_potencial[-2],imoveis_potencial[-1] = imoveis_potencial[-1],imoveis_potencial[-2]

    #display dos dados



    print(f"{"imovel":<15}{"% de economia":^15}{"meta":^15}{"media consumo":^15}{"valor economia":>15}")
    print("="*65)
    for imovel,media_kwh,porcentagem_economica in imoveis_potencial:
        try:
            #nao to fazendo verificação se volta 0 porque os valores enviados sao subtraidos um com o outro
            media_custo_imovel = Calcular_Custo_Kwh(media_kwh)
            meta_custo_imovel = Calcular_Custo_Kwh(imovel["meta_kwh"])
            #if media_custo_imovel <= 0 : continue #descomentar se valores 0 tiver quebrando o codigo
        except Exception as e:
            print("Erro ao calcular custos",e)

        print(f"{imovel["nome"]}  -  {f"{porcentagem_economica:.2f}%"}  -  {imovel["meta_kwh"]}  -  {media_kwh}  -  R${(meta_custo_imovel - media_custo_imovel):.2f}")
        
        print("-"*65)

    

        


    
        
