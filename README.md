# Monitoramento-Energia-Eletrica
Aplicação de terminal que organiza e analisa informações de consumo de energia elétrica de imóveis (residenciais, comerciais e industriais). O sistema realiza várias operações em uma mesma execução e mantém o estado dos dados em memória. Os valores exibidos nunca são pré-calculados: mudam conforme os dados cadastrados.

Equipe: Carlos Daniel + Dante Alves Melgaço

<pre>
    cadastrar_imovel
    registrar_consumo
    calcular_custo
    comparar_meses
    verificar_alerta
    buscar_registro
    atualizar_registro
    calcular_economia
    gerar_relatorio
</pre>
   

os dados vem de um arquivo proprio para guardar-los utils/dados.py (dados com necessidade de usalos em mais de um lugar)

<pre>
recebe entrada, nome e função executavel
em inexistencia de funcao tratar usando if opcao_selecionada == "n":
em caso de nao haver tratamento entrara no exept 
opcoes = { 
    "1":["Cadastrar imóvel",cadastrar_imovel],
    "9":["Sair"]
}
</pre>
https://www.figma.com/board/tO5nIw45uXCCfHMgdXuxlx/projeto?node-id=0-1&t=n0JFYnqa4io5GwCW-0
