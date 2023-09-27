import matplotlib.pyplot as plt
import seaborn as sns

def print_likes(bandas):
    """
    Gera um gráfico de barras mostrando o total de 'likes' para cada banda.

    Parâmetros:
        bandas (list): Uma lista contendo tuplas onde cada tupla contém o nome da banda
                       e um DataFrame de dados.

    Exemplo de Uso:
        >>> dados_bandas = [('Banda A', df_a), ('Banda B', df_b)]
        >>> print_likes(dados_bandas)
    """
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Likes'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais)
    plt.xlabel("Total de Likes")
    plt.ylabel("Bandas")
    plt.title("Total de Likes por Banda")
    plt.show()

def print_views(bandas):
    """
    Gera um gráfico de barras mostrando o total de 'views' para cada banda.

    Parâmetros:
        bandas (list): Uma lista contendo tuplas onde cada tupla contém o nome da banda
                       e um DataFrame de dados.

    Exemplo de Uso:
        >>> dados_bandas = [('Banda A', df_a), ('Banda B', df_b)]
        >>> print_views(dados_bandas)
    """
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Views'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="green")
    plt.xlabel("Total de Views")
    plt.ylabel("Views")
    plt.title("Total de Views por Banda")
    plt.show()

def print_instrumentalidade(bandas):
    """
    Gera um gráfico de barras mostrando a soma da 'instrumentalidade' para cada banda.

    Parâmetros:
        bandas (list): Uma lista contendo tuplas onde cada tupla contém o nome da banda
                       e um DataFrame de dados.

    Exemplo de Uso:
        >>> dados_bandas = [('Banda A', df_a), ('Banda B', df_b)]
        >>> print_instrumentalidade(dados_bandas)
    """
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Instrumentalness'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="orange")
    plt.xlabel("Total de Instrumentalidade")
    plt.ylabel("Instrumentalidade")
    plt.title("Total de Instrumentalidade por Banda")
    plt.show()

def print_valencia(bandas):
    """
    Gera um gráfico de barras mostrando a soma da 'valência' para cada banda.

    Parâmetros:
        bandas (list): Uma lista contendo tuplas onde cada tupla contém o nome da banda
                       e um DataFrame de dados.

    Exemplo de Uso:
        >>> dados_bandas = [('Banda A', df_a), ('Banda B', df_b)]
        >>> print_valencia(dados_bandas)
    """
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Valence'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="purple")
    plt.xlabel("Total de Valência")
    plt.ylabel("Valência")
    plt.title("Total de Valência por Banda")
    plt.show()

def relacao_likes_views(bandas):
    """
    Gera gráficos de dispersão mostrando a relação entre 'Likes' e 'Views' para cada banda.
    Cada gráfico possui uma linha de regressão linear e a variável "Artist" é utilizada como 
    matiz (hue) para diferenciar os dados de diferentes artistas/bandas.

    Parâmetros:
        bandas (list): Uma lista contendo tuplas onde cada tupla contém o nome da banda
                       e um DataFrame de dados.

    Exemplo de Uso:
        >>> dados_bandas = [('Banda A', df_a), ('Banda B', df_b)]
        >>> teste(dados_bandas)
    """
    for banda, dados in bandas:
        sns.lmplot(x='Likes', y='Views', data=dados, fit_reg=True, hue='Artist')
        plt.title(f"Relação entre Likes e Views para {banda}")
        plt.show()
