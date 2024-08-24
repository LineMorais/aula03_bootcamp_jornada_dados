# %% Estruturas de Controle de Fluxo

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para quantidadee preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" 
# se ambos forem positivos ou "Dados inválidos" caso contrário.
try: 
    quantidade = float(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: '))
   
    if quantidade > 0 and preco > 0:
       print('valores validos')
    else:
       print('valores invalidos')

except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# %% Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem proporção de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# 
# Temperatura < 18°C ​​é 'Baixa'
# Temperatura >= 18°C ​​e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


#%% Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 
# 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem 
# com severidade para 'ERROR'.

# %% Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados dos usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e 
# tenha fornecido um e-mail válido. Escreva um programa que valide essas 
# condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# %% Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e 
# precisa identificar transações suspeitas. Uma transação é considerada 
# suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário
# comercial (antes das 9h ou depois das 18h). Dada uma transação como 
# transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# %%