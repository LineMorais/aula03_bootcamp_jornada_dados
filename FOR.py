# %% Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
# Texto:"a raposa marrom salta sobre o cachorro preguiçoso"

texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)

# %% Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)

normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

# %% Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando.
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos =  [usuarios for usuarios in usuarios if usuarios["email"]]

print(usuarios_validos)

# %% Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1, 11)

pares = [x for x in numeros if x % 2 == 0]

print(pares)

# %% Agregação de Dados por Categoria
#Objetivo: Dado um conjunto de registros de vendas, calcular 
# o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = vendas["categoria"]
    valor = vendas["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor
print(total_por_categoria)

