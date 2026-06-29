#%% Exemplo de Uso do while em Engenharia de Dados
# Um cenário comum em engenharia de dados é a necessidade de 
# executar uma tarefa de maneira periódica, como verificar novos 
# dados em um diretório, fazer polling de uma API para novas 
# respostas ou monitorar mudanças em um banco de dados. Nestes casos, 
# um loop while pode ser utilizado para manter o script rodando continuamente
# ou até que uma condição específica seja atingida (por exemplo, 
# um sinal para desligar ou uma condição de erro).
# import time

# while True:
#     print("Verificando novos dados...")
#     # Aqui você pode adicionar o código para verificar novos dados,
#     # por exemplo, checar a existência de novos arquivos em um diretório,
#     # fazer uma consulta a um banco de dados ou API, etc.

# time.sleep(10)  # Pausa o loop por 10 segundos


# %% Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica 
# ("sair") seja fornecida.

dados = []
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")


# %% Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de 
# um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))
print("Número válido!")

# %%Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de 
# dados é processada em loop até que não haja mais páginas.
pagina_atual = 1
paginas_totais = 5# Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")

# %%Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if False:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

# %% Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um
# valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
     # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1
