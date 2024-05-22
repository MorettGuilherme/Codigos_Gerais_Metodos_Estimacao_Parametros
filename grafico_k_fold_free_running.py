# Projeto ATLAS - Reconstrução de sinal - (MÉTODO).
# Autor: Guilherme Barroso Morett.
# Data: 07 de maio de 2024.

# Objetivo do código: construção do gráfico da validação cruzada K-Fold.

""" Organização do código:

Funções presentes:

1) Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
Entrada: número de ocupação.
Saída: matriz com os dados da ocupação organizados de acordo com a coluna (número do janelamento, média, variância e desvio padrão do dado estatístico)

2) Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
Obs.: esse gráfico mostra a média do dado estatatístico (média, variância e desvio padrão do erro de estimação (PARÂMETRO)) com as barras de erro para cada um dos janelamentos ao decorrer das ocupações.
Entrada: matriz com os dados da ocupação organizados.
Saída: nada.

3) Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
Obs.: esse gráfico mostra a média do dado estatatístico (média, variância e desvio padrão do erro de estimação (PARÂMETRO)) com as barras de erro para cada uma das ocupações ao decorrer do janelamento.
Entrada: matriz com os dados da ocupação organizados.
Saída: nada.

4) Instrução principal (main) do código.
Entrada: nada.
Saída: nada.

"""

# Importação de bibliotecas.
import numpy as np
import os
import matplotlib.pyplot as plt
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico da validação cruzada K-Fold para o método (MÉTODO):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### --------------------------- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DA VALIDAÇÃO CRUZADA K-FOLD ------------------------------------ ###

# Definição da função para a leitura dos dados estatísticos do K-Fold.
def leitura_dados_estatisticos_k_fold(n_ocupacao, dado_estatistico):
    
    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos do K-Fold.
    pasta_dados_k_fold = f"K_Fold_{dado_estatistico}_Dados_Estatisticos_Metodo_OC"

    # Nome do arquivo de entrada dos dados estatísticos do K-Fold.
    arquivo_dados_k_fold = f"k_fold_{dado_estatistico}_dados_estatisticos_metodo_OC_{n_ocupacao}.txt"

    # O caminho para esse arquivo de entrada dos dados estatísticos do K-Fold.
    caminho_arquivo_dados_k_fold = os.path.join(pasta_dados_k_fold, arquivo_dados_k_fold)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_k_fold):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_k_fold,"r") as arquivo_entrada_ocupacoes:
        
            # Armazena os dados na variável Matriz_dados_k_fold.
            Matriz_dados_k_fold = np.array(np.loadtxt(arquivo_entrada_ocupacoes, skiprows = 1, dtype='double', delimiter=','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_k_fold} não existe na pasta {pasta_dados_k_fold}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_dados_k_fold.
    return Matriz_dados_k_fold

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------ 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO GRÁFICO DO TIPO A DA VALIDAÇÃO CRUZADA K-FOLD ----------------------------- ###

# Definição da função para a construção do gráfico tipo A pela validação cruzada K-Fold.
def grafico_A_k_fold(opcao, Matriz_dados_k_fold_OC_0, Matriz_dados_k_fold_OC_10, Matriz_dados_k_fold_OC_20, Matriz_dados_k_fold_OC_30, Matriz_dados_k_fold_OC_40, Matriz_dados_k_fold_OC_50, Matriz_dados_k_fold_OC_60, Matriz_dados_k_fold_OC_70, Matriz_dados_k_fold_OC_80, Matriz_dados_k_fold_OC_90, Matriz_dados_k_fold_OC_100):
    
    # Definição da variável indice_coluna_janelamento que armazena o índice da coluna do janelamento.
    indice_coluna_janelamento = 0
    
    # Definição da variável indice_coluna_media que armazena o índice da coluna das médias do dado estatístico.
    indice_coluna_medias = 1
    
    # Definição da variável indice_coluna_DP que armazena o índice da coluna dos desvios padrões do dado estatístico.
    indice_coluna_DP = 3
    
    # Definição do vetor do eixo das abscissas.
    janelamento = Matriz_dados_k_fold_OC_0[:, indice_coluna_janelamento]
    
    # Nomeação do eixo das abscissas.
    plt.xlabel("Quantidade de janelamento", fontsize = 18)
    
    # COmando para o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 18)
    
    # Comando para o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Caso opcao seja 1:
    if opcao == 1:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média da média do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 2.
    elif opcao == 2:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média da var. do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 3.
    elif opcao == 3:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média do DP. do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
        
    # Armazenamento dos dados referentes a ocupação 0.
    Matriz_dados_medias_k_fold_OC_0 = Matriz_dados_k_fold_OC_0[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_0 = Matriz_dados_k_fold_OC_0[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 10.
    Matriz_dados_medias_k_fold_OC_10 = Matriz_dados_k_fold_OC_10[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_10 = Matriz_dados_k_fold_OC_10[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 20.
    Matriz_dados_medias_k_fold_OC_20 = Matriz_dados_k_fold_OC_20[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_20 = Matriz_dados_k_fold_OC_20[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 30.
    Matriz_dados_medias_k_fold_OC_30 = Matriz_dados_k_fold_OC_30[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_30 = Matriz_dados_k_fold_OC_30[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 40.
    Matriz_dados_medias_k_fold_OC_40 = Matriz_dados_k_fold_OC_40[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_40 = Matriz_dados_k_fold_OC_40[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 50.
    Matriz_dados_medias_k_fold_OC_50 = Matriz_dados_k_fold_OC_50[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_50 = Matriz_dados_k_fold_OC_50[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 60.
    Matriz_dados_medias_k_fold_OC_60 = Matriz_dados_k_fold_OC_60[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_60 = Matriz_dados_k_fold_OC_60[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 70.
    Matriz_dados_medias_k_fold_OC_70 = Matriz_dados_k_fold_OC_70[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_70 = Matriz_dados_k_fold_OC_70[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 80.
    Matriz_dados_medias_k_fold_OC_80 = Matriz_dados_k_fold_OC_80[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_80 = Matriz_dados_k_fold_OC_80[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 90.
    Matriz_dados_medias_k_fold_OC_90 = Matriz_dados_k_fold_OC_90[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_90 = Matriz_dados_k_fold_OC_90[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 100.
    Matriz_dados_medias_k_fold_OC_100 = Matriz_dados_k_fold_OC_100[: , indice_coluna_medias]
    Matriz_dados_erros_k_fold_OC_100 = Matriz_dados_k_fold_OC_100[: , indice_coluna_DP]

    # Plote dos dados.
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_0, yerr = Matriz_dados_erros_k_fold_OC_0, color = 'darkviolet', linestyle = '--', marker = 'o', markersize = 3, label = '0')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_10, yerr = Matriz_dados_erros_k_fold_OC_10, color = 'violet', linestyle = '--', marker = 'o', markersize = 3, label = '10')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_20, yerr = Matriz_dados_erros_k_fold_OC_20, color = 'blue', linestyle = '--', marker = 'o', markersize = 3, label = '20')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_30, yerr = Matriz_dados_erros_k_fold_OC_30, color = 'slateblue', linestyle = '--', marker = 'o', markersize = 3, label = '30')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_40, yerr = Matriz_dados_erros_k_fold_OC_40, color = 'cyan', linestyle = '--', marker = 'o', markersize = 3, label = '40')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_50, yerr = Matriz_dados_erros_k_fold_OC_50, color = 'green', linestyle = '--', marker = 'o', markersize = 3, label = '50')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_60, yerr = Matriz_dados_erros_k_fold_OC_60, color = 'greenyellow', linestyle = '--', marker = 'o', markersize = 3, label = '60')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_70, yerr = Matriz_dados_erros_k_fold_OC_70, color = 'yellow', linestyle = '--', marker = 'o', markersize = 3, label = '70')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_80, yerr = Matriz_dados_erros_k_fold_OC_80, color = 'gold', linestyle = '--', marker = 'o', markersize = 3, label = '80')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_90, yerr = Matriz_dados_erros_k_fold_OC_90, color = 'orange', linestyle = '--', marker = 'o', markersize = 3, label = '90')
    plt.errorbar(janelamento, Matriz_dados_medias_k_fold_OC_100, yerr = Matriz_dados_erros_k_fold_OC_100, color = 'red', linestyle = '--', marker = 'o', markersize = 3, label = '100')
    
    # Comando para o grid do gráfico.
    plt.grid()

    # Comando para a legenda e o posicionamento.
    plt.legend(title = 'Ocupação (OC.)', title_fontproperties = {'weight': 'bold', 'size': 12}, loc = 'upper center', fontsize = 16, ncol = 6)

    # Comando para a exibição do gráfico.
    plt.show()  
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------- 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO GRÁFICO DO TIPO B DA VALIDAÇÃO CRUZADA K-FOLD --------------------------- ###

# Definição da função para a construção do gráfico do tipo B pela validação cruzada K-Fold.
def grafico_B_k_fold(opcao, Matriz_dados_k_fold_OC_0, Matriz_dados_k_fold_OC_10, Matriz_dados_k_fold_OC_20, Matriz_dados_k_fold_OC_30, Matriz_dados_k_fold_OC_40, Matriz_dados_k_fold_OC_50, Matriz_dados_k_fold_OC_60, Matriz_dados_k_fold_OC_70, Matriz_dados_k_fold_OC_80, Matriz_dados_k_fold_OC_90, Matriz_dados_k_fold_OC_100):
    
    # Definição do vetor das ocupações.
    ocupacoes = np.arange(0, 101, 10)
    
    # Definição da variável indice_coluna_media que armazena o índice da coluna das médias do dado estatístico.
    indice_coluna_medias = 1
    
    # Definição da variável indice_coluna_DP que armazena o índice da coluna dos desvios padrões do dado estatístico.
    indice_coluna_DP = 3
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Quantidade de janelamento", fontsize = 18)
    
    # COmando para o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 18)
    
    # Comando para o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Caso opcao seja 1:
    if opcao == 1:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média da média do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 2.
    elif opcao == 2:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média da var. do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 3.
    elif opcao == 3:
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média do DP. do erro de estimação (PARÂMETRO) (ADC Count)", fontsize = 18)
    
    # Definição dos índices para cada um dos janelamentos de acordo com a organização do arquivo de entrada.    
    indice_J7 = 0
    indice_J9 = 1
    indice_J11 = 2
    indice_J13 = 3
    indice_J15 = 4
    indice_J17 = 5
    indice_J19 = 6
        
    # Armazenamentos dos dados referentes ao janelamento 7.
    Matriz_dados_k_fold_J7_OC = [Matriz_dados_k_fold_OC_0[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J7, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J7, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J7_OC = [Matriz_dados_k_fold_OC_0[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J7, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J7, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 9.
    Matriz_dados_k_fold_J9_OC = [Matriz_dados_k_fold_OC_0[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J9, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J9, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J9_OC = [Matriz_dados_k_fold_OC_0[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J9, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J9, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 11.
    Matriz_dados_k_fold_J11_OC = [Matriz_dados_k_fold_OC_0[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J11, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J11, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J11_OC = [Matriz_dados_k_fold_OC_0[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J11, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J11, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 13.
    Matriz_dados_k_fold_J13_OC = [Matriz_dados_k_fold_OC_0[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J13, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J13, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J13_OC = [Matriz_dados_k_fold_OC_0[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J13, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J13, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 15.
    Matriz_dados_k_fold_J15_OC = [Matriz_dados_k_fold_OC_0[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J15, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J15, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J15_OC = [Matriz_dados_k_fold_OC_0[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J15, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J15, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 17.
    Matriz_dados_k_fold_J17_OC = [Matriz_dados_k_fold_OC_0[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J17, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J17, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J17_OC = [Matriz_dados_k_fold_OC_0[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J17, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J17, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 19.
    Matriz_dados_k_fold_J19_OC = [Matriz_dados_k_fold_OC_0[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_10[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_20[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_30[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_40[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_50[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_60[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_70[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_80[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_90[indice_J19, indice_coluna_medias], Matriz_dados_k_fold_OC_100[indice_J19, indice_coluna_medias]]
    Matriz_dados_k_fold_erros_J19_OC = [Matriz_dados_k_fold_OC_0[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_10[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_20[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_30[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_40[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_50[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_60[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_70[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_80[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_90[indice_J19, indice_coluna_DP], Matriz_dados_k_fold_OC_100[indice_J19, indice_coluna_DP]]

    # Plote dos dados.
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J7_OC, yerr = Matriz_dados_k_fold_erros_J7_OC, color = 'violet', linestyle = '--', marker='o', markersize = 3, label = '7')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J9_OC, yerr = Matriz_dados_k_fold_erros_J9_OC, color = 'blue', linestyle = '--', marker='o', markersize = 3, label = '9')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J11_OC, yerr = Matriz_dados_k_fold_erros_J11_OC, color = 'cyan', linestyle = '--', marker='o', markersize = 3, label = '11')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J13_OC, yerr = Matriz_dados_k_fold_erros_J13_OC, color = 'green', linestyle = '--', marker='o', markersize = 3, label = '13')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J15_OC, yerr = Matriz_dados_k_fold_erros_J15_OC, color = 'yellow', linestyle = '--', marker='o', markersize = 3, label = '15')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J17_OC, yerr = Matriz_dados_k_fold_erros_J17_OC, color = 'orange', linestyle = '--', marker='o', markersize = 3, label = '17')
    plt.errorbar(ocupacoes, Matriz_dados_k_fold_J19_OC, yerr = Matriz_dados_k_fold_erros_J19_OC, color = 'red', linestyle = '--', marker='o', markersize = 3, label = '19')
    
    # Comando para o grid do gráfico.
    plt.grid()

    # Comando para a legenda e o posicionamento.
    plt.legend(title = 'Janelamento', title_fontproperties = {'weight': 'bold', 'size': 12}, loc='upper center', fontsize = 16, ncol = 4)
    
    # Comando para a exibição do gráfico.
    plt.show()  
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------------------------- 4) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ----------------------------------------------- ###

# Definição da instrução principal (main) do código.
def principal_grafico_k_fold():
    
    # Impressão de mensagem no terminal.
    print("\nTipos de gráficos:\nNúmero de janelamento versus média do dado estatístico ao decorrer das ocupações: A\nNúmero de ocupações versus média do dado estatístico ao decorrer do janelamento: B")
    
    # A variável tipo_grafico armazena a string digitada pelo usuário via terminal.
    tipo_grafico = str(input("Digite o tipo de gráfico desejado: "))
    
    # A string tipo_grafico é convertida para maiúscula.
    tipo_grafico = tipo_grafico.upper()
    
    # Se a variável tipo_grafico for diferente de "A" ou "B".
    if tipo_grafico != "A" and tipo_grafico != "B":
        
        # Exibição de uma mensagem de alerta de que o tipo de gráfico solicitado é inválido.
        print("Por favor digite uma tipo válido de gráfico: A ou B!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Impressão de mensagem no terminal.
    print("\nOpções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável opcao armazena o número do tipo inteiro digitado pelo usuário via terminal.
    opcao = int(input("Digite o número da opção desejada: "))

    # A variável valores_dados é uma lista com os valores aceitáveis para opcao.
    valores_opcao= list(range(1,4,1))

    # Caso o valor digitado armazenado na variável opcao não estiver presente na lista valores_dados.
    if opcao not in valores_opcao:
    
        # Exibição de uma mensagem de alerta de que a opcao solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Caso opcao seja 1.
    if opcao == 1:
        
        # A variável dado_estatistico recebe a string "media".
        dado_estatistico = "media"
        
    # Caso opcao seja 2.
    elif opcao == 2:
        
        # A variável dado_estatistico recebe a string "var".
        dado_estatistico = "var"
        
    # Caso a opcao seja 3.
    elif opcao == 3:
        
        # A variável dado_estatistico recebe a string "DP".
        dado_estatistico = "DP"
        
    # Chamada das funções.
          
    Matriz_dados_k_fold_OC_0 = leitura_dados_estatisticos_k_fold(0, dado_estatistico)
    Matriz_dados_k_fold_OC_10 = leitura_dados_estatisticos_k_fold(10, dado_estatistico)
    Matriz_dados_k_fold_OC_20 = leitura_dados_estatisticos_k_fold(20, dado_estatistico)
    Matriz_dados_k_fold_OC_30 = leitura_dados_estatisticos_k_fold(30, dado_estatistico)
    Matriz_dados_k_fold_OC_40 = leitura_dados_estatisticos_k_fold(40, dado_estatistico)
    Matriz_dados_k_fold_OC_50 = leitura_dados_estatisticos_k_fold(50, dado_estatistico)
    Matriz_dados_k_fold_OC_60 = leitura_dados_estatisticos_k_fold(60, dado_estatistico)
    Matriz_dados_k_fold_OC_70 = leitura_dados_estatisticos_k_fold(70, dado_estatistico)
    Matriz_dados_k_fold_OC_80 = leitura_dados_estatisticos_k_fold(80, dado_estatistico)
    Matriz_dados_k_fold_OC_90 = leitura_dados_estatisticos_k_fold(90, dado_estatistico)
    Matriz_dados_k_fold_OC_100 = leitura_dados_estatisticos_k_fold(100, dado_estatistico)
    
    # Caso a variável tipo_grafico seja "A".
    if tipo_grafico == "A":
        
        # Chamada da função grafico_A_k_fold.
        grafico_A_k_fold(opcao, Matriz_dados_k_fold_OC_0, Matriz_dados_k_fold_OC_10, Matriz_dados_k_fold_OC_20, Matriz_dados_k_fold_OC_30, Matriz_dados_k_fold_OC_40, Matriz_dados_k_fold_OC_50, Matriz_dados_k_fold_OC_60, Matriz_dados_k_fold_OC_70, Matriz_dados_k_fold_OC_80, Matriz_dados_k_fold_OC_90, Matriz_dados_k_fold_OC_100)
      
    # Caso a variável tipo_grafico seja "B".  
    elif tipo_grafico == "B":
    
        # Chamada da função grafico_B_k_fold.
        grafico_B_k_fold(opcao, Matriz_dados_k_fold_OC_0, Matriz_dados_k_fold_OC_10, Matriz_dados_k_fold_OC_20, Matriz_dados_k_fold_OC_30, Matriz_dados_k_fold_OC_40, Matriz_dados_k_fold_OC_50, Matriz_dados_k_fold_OC_60, Matriz_dados_k_fold_OC_70, Matriz_dados_k_fold_OC_80, Matriz_dados_k_fold_OC_90, Matriz_dados_k_fold_OC_100)
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da função principal do código.
principal_grafico_k_fold()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")   
    
    
    
    