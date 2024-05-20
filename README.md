O objetivo desse repositório é conter os códigos necessários para a aplicação de métodos de estimação de parâmetros na área de processamento de sinais.
A seguir estão listados cada um dos códigos e suas respectivas funções presentes nos arquivos:

1) arquivo_saida_dados_estatisticos_free_running.py
- Cálculo dos dados estatístico do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída.

2) grafico_dado_estatistico_janelamento_free_running.py
- Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento;
- Plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.

3) grafico_k_fold_free_running.py
- Leitura dos dados estatísticos da validação cruzada K-Fold;
- Construção do gráfico tipo A da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada um dos janelamentos ao decorrer das ocupações);
- Construção do gráfico tipo B da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada uma das ocupações ao decorrer do janelamento).
  
4) histograma_erro_amplitude_free_running.py
Obs.: esse arquivo está formatado inicialmente para a amplitude. No entanto, ele também pode ser redigido para a fase.
- Cálculo da estatística do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída;
- Plote do histograma do erro de estimação.

5) k_fold_free_running.py
- Salvar em arquivos os dados estatísticos pela validação cruzada k-Fold;
- Validação cruzada K-Fold.

6) leitura_dados_ocupacao_free_running.py
- Leitura dos dados de ocupação;
- Retirada do pedestal dos pulsos de sinais |(alguns métodos necessitam dessa etapa, como por exemplo o da desconvoluçaõ de sinais);
- Construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência;
- Separação em dados de treino e teste pela metade.


