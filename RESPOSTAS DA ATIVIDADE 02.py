# Atividade 02 – Bootcamp Avanti

# ----------------------------------------
# 1. Função que retorna números ímpares de uma lista
def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

# Teste
print("1. Números ímpares:", numeros_impares([1, 2, 3, 4, 5, 6]))

# ----------------------------------------
# 2. Função que retorna os números primos de uma lista
def numeros_primos(lista):
    primos = []
    for n in lista:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                primos.append(n)
    return primos

# Teste
print("2. Números primos:", numeros_primos([2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ----------------------------------------
# 3. Função que retorna os elementos únicos entre duas listas
def elementos_unicos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

# Teste
print("3. Elementos únicos:", elementos_unicos([1, 2, 3], [3, 4, 5]))

# ----------------------------------------
# 4. Função que retorna o segundo maior valor da lista
def segundo_maior(lista):
    lista = list(set(lista))  # Remove duplicados
    lista.sort()
    if len(lista) < 2:
        return None
    return lista[-2]

# Teste
print("4. Segundo maior valor:", segundo_maior([10, 20, 30, 40]))

# ----------------------------------------
# 5. Ordenar lista de tuplas pelo nome (ordem alfabética)
def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda x: x[0])

# Teste
pessoas = [('Maria', 30), ('Ana', 25), ('João', 35)]
print("5. Ordenado por nome:", ordenar_por_nome(pessoas))

# ----------------------------------------
# 6. Identificar e remover outliers usando quartis
import pandas as pd

def tratar_outliers(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    df_sem_outliers = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
    return df_sem_outliers

# Teste
df_outliers = pd.DataFrame({'valores': [10, 12, 14, 15, 1000]})
print("6. DataFrame sem outliers:\n", tratar_outliers(df_outliers, 'valores'))

# ----------------------------------------
# 7. Concatenar DataFrames mesmo com colunas diferentes
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})

concat_linhas = pd.concat([df1, df2], axis=0)
concat_colunas = pd.concat([df1, df3], axis=1)

print("7. Concatenado por linhas:\n", concat_linhas)
print("\nConcatenado por colunas:\n", concat_colunas)

# ----------------------------------------
# 8. Leitura de arquivo CSV e exibição das primeiras linhas

import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('alunos.csv')  # troque pelo nome do seu arquivo

# Mostra as primeiras 5 linhas
print(df.head())

# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

import pandas as pd

df = pd.DataFrame({'nome': ['Ana', 'João', 'Maria'], 'idade': [22, 35, 17]})

# Selecionar coluna 'idade'
print(df['idade'])

# Filtrar pessoas com idade maior que 18
print(df[df['idade'] > 18])

#10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Ana', 'João', 'Maria'],
    'idade': [22, np.nan, 17]
})

# Ver onde há NaN
print(df.isna())

# Preencher NaN com 0
print(df.fillna(0))

# Remover linhas com NaN
print(df.dropna())
