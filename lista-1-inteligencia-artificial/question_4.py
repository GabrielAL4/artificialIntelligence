import numpy as np
import pandas as pd

def ler_arquivo_excel():
    """
    Lê um arquivo Excel contendo dados climáticos e extrai as temperaturas média, mínima e máxima.

    Returns:
        tuple: Uma tupla contendo as temperaturas média, mínima e máxima como NumPy arrays.
    """
    dataFrame = pd.read_excel('Dados_climaticos_historicos.xlsx', sheet_name='Historico_Clima_Rio_de_Janeiro', header=3)
    temperatura_media = dataFrame.iloc[0, 1:].values.astype(float)
    temperatura_minima = dataFrame.iloc[1, 1:].values.astype(float)
    temperatura_maxima = dataFrame.iloc[2, 1:].values.astype(float)
    return temperatura_media, temperatura_minima, temperatura_maxima

def salvar_em_arquivo(dados, nome_arquivo):
    """
    Salva um conjunto de dados em um arquivo ASCII.

    Args:
        dados (numpy.ndarray): Os dados a serem salvos.
        nome_arquivo (str): O nome do arquivo onde os dados serão salvos.
    """
    np.savetxt(nome_arquivo, dados, delimiter='\t')

def carregar_de_arquivo(nome_arquivo):
    """
    Carrega dados de um arquivo ASCII em um NumPy array.

    Args:
        nome_arquivo (str): O nome do arquivo a ser carregado.

    Returns:
        numpy.ndarray: Os dados carregados do arquivo.
    """
    return np.loadtxt(nome_arquivo, delimiter='\t')

def encontrar_maximo_minimo_temp_media(dados):
    """
    Encontra o máximo e o mínimo na coluna de temperatura média.

    Args:
        dados (numpy.ndarray): Um array contendo os dados de temperatura.

    Returns:
        tuple: Uma tupla contendo o máximo e o mínimo da temperatura média.
    """
    temp_media = dados[:, 0]
    max_temp_media = np.max(temp_media)
    min_temp_media = np.min(temp_media)
    return max_temp_media, min_temp_media

# ... (outras funções de operações omitidas para economizar espaço)

def main():
    """
    Função principal que executa todas as operações.
    """
    temperatura_media, temperatura_minima, temperatura_maxima = ler_arquivo_excel()
    dados_temperaturas = np.vstack((temperatura_media, temperatura_minima, temperatura_maxima)).T
    salvar_em_arquivo(dados_temperaturas, 'temperaturas_rio_de_janeiro.txt')
    dados_carregados = carregar_de_arquivo('temperaturas_rio_de_janeiro.txt')
    
    print("Dimensão do array:", dados_carregados.shape)
    max_temp_media, min_temp_media = encontrar_maximo_minimo_temp_media(dados_carregados)
    print("Máximo valor na coluna de temperatura média:", max_temp_media)
    print("Mínimo valor na coluna de temperatura média:", min_temp_media)
    
    # ... (chama outras funções de operações)

if __name__ == "__main__":
    main()
