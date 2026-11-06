import utils.menu as menu
from utils.cadastrar_imovel import Cadastrar_Imovel

opcoes = {
    "1":["Cadastrar imóvel",Cadastrar_Imovel],
    "2":["Registrar consumo"],
    "3":["Buscar imóveis"],
    "4":["Atualizar registro"],
    "5":["Comparar meses"],
    "6":["Alertas"],
    "7":["Economia potencial"],
    "8":["Relatório consolidado"],
    "9":["Sair"]
}

while True :
    opcao_selecionada = menu.Display_Menu(opcoes)

    if opcao_selecionada == "9" : 
        print("bye")
        break

    try:
        opcoes[opcao_selecionada][1]()
    except Exception as e:
        print("Opção sem funcionalide ou erro ao iniciala")
    