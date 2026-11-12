import utils.menu as menu
from dados.dados import imoveis
#puxa so a função envez do arquivo completo
from utils.cadastrar_imovel import Cadastrar_Imovel
from utils.registrar_consumo import Registrar_Consumo
from utils.buscar_imoveis import Buscar_Imoveis
from utils.buscar_registros import Buscar_Registros
from utils.atualizar_registro import Atualizar_Registro
from utils.comparar_meses import Comparar_Meses
from utils.alertas import Alertas
from utils.economia_potencial import Economia_Potencial
from utils.relatorio import Relatorio

opcoes = {
    #recebe entrada, nome e função executavel
    #em inexistencia de funcao tratar usando if opcao_selecionada == "n":
    #se nao haver tratamento vai entrar no exept (tentar nao deixar chegar nesse caso)
    "1":["Cadastrar imóvel",Cadastrar_Imovel],
    "2":["Registrar consumo",Registrar_Consumo],
    "3":["Buscar imóveis",Buscar_Imoveis],
    "4":["Buscar registros",Buscar_Registros],
    "5":["Atualizar registro",Atualizar_Registro],
    "6":["Comparar meses",Comparar_Meses],
    "7":["Alertas",Alertas],
    "8":["Economia potencial",Economia_Potencial],
    "9":["Relatório consolidado",Relatorio],
    "0":["Sair"],
}

try:
    while True :
        opcao_selecionada = menu.Display_Menu(opcoes)
        
        if opcao_selecionada == "0":
            print("bye")
            break 

        try:
            #funcao das opcoes tem que ser chamadas sem nada
            opcoes[opcao_selecionada][1]()
        except Exception as e:
            print("Opção sem funcionalide ou erro ao inicia-la (tente novamete) - ",e)
except KeyboardInterrupt:
    print("\nbye")