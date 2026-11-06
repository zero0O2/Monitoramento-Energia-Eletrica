import menu

opcoes = {
    "1":"Cadastrar imóvel",
    "2":"Registrar consumo",
    "3":"Buscar por ID",
    "4":"Atualizar registro",
    "5":"Comparar meses",
    "6":"Alertas",
    "7":"Economia potencial",
    "8":"Relatório consolidado",
    "9":"Sair",
}

opcao_selecionada = menu.Display_Menu(opcoes)
print(f"escolheu {opcao_selecionada}")
