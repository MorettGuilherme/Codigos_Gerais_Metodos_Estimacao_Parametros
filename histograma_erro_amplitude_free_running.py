# Projeto Atlas - Reconstrução de sinal - (MÉTODO).
# Autor: Guilherme Barroso Morett.
# Data: 07 de maio de 2024.

# Objetivo do código: análise do erro absoluto do parâmetro (PARÂMETRO) pelo método (MÉTODO) - Free-running.

""" Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao.py
Método: (ARQUIVO PY DO MÉTODO)

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação (PARÂMETRO).
Entrada: lista com os erros de estimação (PARÂMETRO).
Saída: a média, a variância e o desvio padrão do erro de estimação (PARÂMETRO).

2) Função para salvar os dados estatísticos do erro de estimação (PARÂMETRO) para determinada ocupação em uma arquivo de saída.
Entrada: a média, a variância e o desvio padrão do erro de estimação (PARÂMETRO).
Saída: nada.

3) Função para o plote do histograma do erro de estimação (PARÂMETRO).
Entrada: lista com os erros de estimação (PARÂMETRO) e seus dados estatatísticos.
Saída: nada.

4) Função principal.
Entrada: nada.
Saída: nada.

"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from leitura_dados_ocupacao_free_running import *
#from arquivo_metodo import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação (PARÂMETRO) pelo método (MÉTODO):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### -------------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO (PARÂMETRO) ------------------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação (PARÂMETRO).
def dados_estatisticos_erro_parametro(lista_erro_parametro):
    
    # A lista do erro de estimação (PARÂMETRO) é convertida para o tipo numpy array.
    vetor_erro_parametro = np.array(lista_erro_parametro)

    # Cálculo da média do erro de estimação (PARÂMETRO).
    media_erro_parametro = np.mean(vetor_erro_parametro)

    # Cálculo da variância do erro de estimação (PARÂMETRO).
    var_erro_parametro = np.var(vetor_erro_parametro)

    # Cálculo do desvio padrão do erro de estimação (PARÂMETRO).
    desvio_padrao_erro_parametro = np.std(vetor_erro_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação (PARÂMETRO).
    return media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------ 2) FUNÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO ERRO DE ESTIMAÇÃO (PARÂMETRO) ---------------------------------- ###

# Definição de função para a confecção do histograma do erro de estimação (PARÂMETRO).
def histograma_erro_parametro(n_ocupacao, lista_erro_parametro, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro):
    
    # A lista do erro de estimação (PARÂMETRO) é convertida para o tipo numpy array.
    vetor_erro_parametro = np.array(lista_erro_parametro)

    # Nomeação do eixo x de acordo com os demais parâmetros.
    plt.xlabel('Erro de estimação (PARÂMETRO) (ADC Count)', fontsize = 18)

    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_parametro, 6)} \n Variância: {round(var_erro_parametro, 6)} \n Desvio padrão: {round(desvio_padrao_erro_parametro, 6)}"

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_parametro, bins = 100, range = [-200, 200], edgecolor='black', linewidth=1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)
    
    # Comando para o título do gráfico.
    plt.title(f"Ocupação (OC.) = {n_ocupacao}", fontsize = 18)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------- 3) FUNÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO (PARÂMETRO) EM UM ARQUIVO DE SAÍDA ---------------- ###

def arquivo_saida_dados_estatisticos_erro_parametro(n_ocupacao, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_erro,desvio_padrao_erro\n"

    # Definição da pasta em que contém o arquivo de saída.
    pasta_saida = "Dados_Estatisticos_Metodo_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = "dados_estatisticos_metodo.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_parametro},{var_erro_parametro},{desvio_padrao_erro_parametro}\n")
        # Impressão no terminal de que a operação foi um sucesso.
        print(f"O arquivo dos dados estatísticos para a ocupação {n_ocupacao} foi atualizado com sucesso!")
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 4) FUNÇÃO PRINCIPAL (MAIN) -------------------------------------------------------------------------- ###

# Definição da função principal (main) do código.
def principal_histograma_erro_parametro():
    
    # A variável n_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável n_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)

    # Chamada ordenada das funções.
    
    Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
    
    Matriz_Dados_OC_sem_pedestal = retirada_pedestal(Matriz_Dados_OC)
    
    vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC_sem_pedestal)
    
    Matriz_dados_pulsos, vetor_parametro_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
    lista_erro_parametro = []
    
    #lista_erro_parametro = arquivo_metodo(Matriz_dados_pulsos, vetor_parametro_referencia, n_janelamento)
    
    media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro = dados_estatisticos_erro_parametro(lista_erro_parametro)
    
    histograma_erro_parametro(n_ocupacao, lista_erro_parametro, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro)
    
    arquivo_saida_dados_estatisticos_erro_parametro(n_ocupacao, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro)
    
# Chamada da função principal (main) do código.
principal_histograma_erro_parametro()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

