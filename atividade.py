import csv

# Função para carregar os dados de um arquivo CSV
def carregar_dados(arquivo, separador, tipos):
    dados = []
    with open(arquivo, 'r') as f:
        reader = csv.DictReader(f, delimiter=separador)
        for row in reader:
            # Converte os valores para os tipos especificados
            for coluna, tipo in tipos.items():
                row[coluna] = tipo(row[coluna])
            dados.append(row)
    return dados

# Função para salvar os dados em um arquivo CSV
def salvar_dados(dados, arquivo, separador):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=dados[0].keys(), delimiter=separador)
        writer.writeheader()
        writer.writerows(dados)

# Função para acessar registros por índice
def acessar_registros_por_indice(dados, indices):
    return [dados[i] for i in indices]

# Função para acessar registros por intervalo de índices
def acessar_registros_por_intervalo(dados, inicio, fim):
    return dados[inicio:fim+1]

# Função para selecionar registros baseado em uma condição
def selecionar_registros(dados, condicao):
    return [registro for registro in dados if condicao(registro)]

# Função para projetar apenas alguns campos dos dados
def projetar_campos(dados, campos):
    return [{campo: registro[campo] for campo in campos} for registro in dados]

# Função para atualizar registros de acordo com uma condição
def atualizar_registros(dados, condicao, campo, valor):
    for registro in dados:
        if condicao(registro):
            registro[campo] = valor

# Função para agrupar registros por um atributo comum
def agrupar_registros(dados, atributo):
    grupos = {}
    for registro in dados:
        valor = registro[atributo]
        if valor in grupos:
            grupos[valor].append(registro)
        else:
            grupos[valor] = [registro]
    return grupos