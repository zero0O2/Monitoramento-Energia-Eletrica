
#Os dados iniciais pra gente testar as funcionalidades
#importar as variaveis que for usar (imoveis, registros) envez de arquivo completo

#Modelos - caso necessario
#{"id":(indentificador),"nome":"nome imovel","tipo":"(residencial,comercial ou industrial)","meta_kwh":200}
#{"id":(indentificado),"id_imovel":2,"mes":"2026-01","kwh":180}

#Os id dos novos valores vao ser o id do ultimo valor + 1

#pra usar a tabela ja fiz uma funcao dentro de func.calcular_custo_kwh
#nome da funcao Calcular_Custo_Kwh
#ela recebe apenas o valor em kwh (ex:230) e ja retorna o valor gasto,ta um pouco confuso mas funciona
tabela_consumo = [
    [(0,100),0.6],
    [(101,200),0.8],
    [(201,300),1.0],
    [(301,"x"),1.3]
]

imoveis = [
    {
        "id": 0,
        "nome": "Casa Grande na Praia",
        "tipo": "residencial",
        "meta_kwh": 250
    },
    {
        "id": 1,
        "nome": "Comercio Ze das Tapioca",
        "tipo": "comercial",
        "meta_kwh": 160
    },
    {
        "id": 2,
        "nome": "Fabrica de Chapeu",
        "tipo": "industrial",
        "meta_kwh": 160
    }
]

registros = [
    {
        "id": 0,
        "id_imovel": 0,
        "data": "2026-07",
        "kwh": 230
    },
    {
        "id": 1,
        "id_imovel": 0,
        "data": "2026-08",
        "kwh": 260
    },
    {
        "id": 2,
        "id_imovel": 0,
        "data": "2026-09",
        "kwh": 194
    },
    {
        "id": 3,
        "id_imovel": 0,
        "data": "2026-10",
        "kwh": 245
    },
    {
        "id": 4,
        "id_imovel": 1,
        "data": "2026-07",
        "kwh": 150
    },
    {
        "id": 5,
        "id_imovel": 1,
        "data": "2026-08",
        "kwh": 15
    },
    {
        "id": 6,
        "id_imovel": 1,
        "data": "2026-09",
        "kwh": 140
    },
    {
        "id": 7,
        "id_imovel": 1,
        "data": "2026-10",
        "kwh": 190
    },
    {
        "id": 8,
        "id_imovel": 2,
        "data": "2026-07",
        "kwh": 165
    },
    {
        "id": 9,
        "id_imovel": 2,
        "data": "2026-08",
        "kwh": 145
    },
    {
        "id": 10,
        "id_imovel": 2,
        "data": "2026-09",
        "kwh": 210
    },
    {
        "id": 11,
        "id_imovel": 2,
        "data": "2026-10",
        "kwh": 180
    }
]