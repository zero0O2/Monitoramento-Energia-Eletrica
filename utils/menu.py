def Display_Menu(opcoes):
    print("\n\n"+"="*45)
    print(f"{' Monitoramento de Energia Elétrica '.upper(): ^45}")
    print("="*45)
    print(f"{"Selecione uma das opções": ^45}\n")

    for opcao in opcoes:
        print(f"{f'{opcao} {' ' + opcoes[opcao][0]:->30}':^45}")
    print("")

    while True:
        #se tiver a opção no dic recebido retorna APENAS a chave do obj
        opcao_selecionada = input("Selecione: ")
        if opcao_selecionada not in opcoes:
            print("Opção selecionada não disponivel\n")
            continue
        return opcao_selecionada