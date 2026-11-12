#pra usar a tabela ja fiz uma funcao dentro de func.calcular_custo_kwh
#nome da funcao Calcular_Custo_Kwh
#ela recebe apenas o valor em kwh (ex:230) e ja retorna o valor gasto,ta um pouco confuso mas funciona
# IMPORTANTE se vier um valor negativo ou zero ela retorna zero,(fazer verificação apos uso)

from dados.dados import tabela_consumo 
def Calcular_Custo_Kwh(kwh):
    if kwh <= 0:
        return 0
    
    custo_total = 0
    kwh_baixa = kwh
    for faixa in tabela_consumo:
        if faixa[0][1] == "x":
            custo_total += kwh_baixa * faixa[1]
            kwh_baixa = 0
        elif kwh_baixa > faixa[0][1] - faixa[0][0]:
            custo_total += (faixa[0][1] - faixa[0][0]) * faixa[1]
            kwh_baixa -= faixa[0][1] - faixa[0][0]
        else:
            custo_total += kwh_baixa * faixa[1]
            kwh_baixa = 0
            
    return custo_total