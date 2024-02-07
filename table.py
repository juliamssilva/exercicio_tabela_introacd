# Júlia Moraes da Silva 20230014434

# Função para criar a tabela
def criar_tabela(colunas,valores):
    if len(colunas) != len(valores):
        return ('Erro ao criar tabela')
        
    dicionario = {coluna: [] for coluna in colunas}

    for i in range(len(colunas)):
        coluna = colunas[i]
        for valor in valores[i]:
            dicionario[coluna].append(valor)
    return dicionario
        
#Adicionar linha 
def adicionar_linha(dicionario,lista):

    if len(dicionario)>len(lista):
        return ("Não foi possível adicionar a linha por falta de valores")
    
    i = 0
    for chave in dicionario:
        dicionario[chave].append(lista[i])
        i += 1
     
    return dicionario

#Remover linha
def remover_linha(dicionario, indice):
    for chave,lista in dicionario.items():
        if not (0<= indice <= len(lista)):
            return ("Esse índice não existe nesse dicionário")
        else:
            del lista[indice]
            
    return dicionario

#Adicionar a coluna 
def adicionar_coluna(dicionario,chave,info):
    dicionario[chave]= info
    return dicionario

#Remover coluna 
def remover_coluna(dicionario,chave):
    if chave not in dicionario:
        return print('Essa chave não existe nesse dicionário')
    else:
        del dicionario[chave]
    return dicionario 

#Somar coluna
def somar_coluna(dicionario):
    resultado = []
    for chave,lista in dicionario.items():
        if (type(lista[0]) == int or type(lista[0]) == float):
            resultado.append(f'Soma de {chave}: {sum(lista)}')
    return resultado

#Média das colunas 
def media_coluna(dicionario):
    resultado = []
    for chave,lista in dicionario.items():
        if (type(lista[0]) == int or type(lista[0]) == float):
            resultado.append(f'Média de {chave}: {sum(lista)/len(lista):.2f}')
    return resultado

#Exibir a tabela
def exibir_tabela (dicionario):
    for chave in dicionario.keys():
        print("_" * len(chave), end="_________")
    print()
    for chave in dicionario.keys():
        print(f"{chave:<15}",end=" ")
    print()
    for chave in dicionario.keys():
        print("_" * len(chave), end="_________")
    primeira = next(iter(dicionario))    
    entradas = len(dicionario[primeira])
    for i in range(entradas):
        print()
        for chave in dicionario.keys():
            print(f"{dicionario[chave][i]:<15}", end=" ")
    print()
    for chave in dicionario.keys():
        print("_" * len(chave), end="_________")

#Abrir CSV
def abrir_csv(arquivo):
    caminho_arquivo = arquivo
    dicionario = {}
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        linha_chaves = arquivo_csv.readline()
        linha_chaves = linha_chaves.strip('').split(';')
        linha_chaves = linha_chaves[:-1]
        for chave in linha_chaves:
            dicionario[chave] = []
        for linha in arquivo_csv:
            info = linha.strip().split(';')
            info = info[:-1]
            for chave, valor in zip(linha_chaves,info):
                dicionario[chave].append(valor)

    return dicionario

#Função que verifica se a idde é maior que 18
def verific_idade(dicionario):
    lista= []
    for i,item in enumerate(dicionario['Idade']):
        if item > 26:
            lista.append(i)
    return lista

#Função de filtrar 
def filtro(dicionario, funcao):
    indices = funcao(dicionario)
    resultado = []
    for item in indices:
        linhas = {chave: dicionario[chave][item] for chave in dicionario}
        resultado.append(linhas)

    return resultado

    
    
