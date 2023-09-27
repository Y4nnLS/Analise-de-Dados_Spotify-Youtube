import matplotlib.pyplot as plt
import seaborn as sns

def print_likes(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Likes'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais)
    plt.xlabel("Total de Likes")
    plt.ylabel("Bandas")
    plt.title("Total de Likes por Banda")
    plt.show()

def print_views(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Views'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="green")
    plt.xlabel("Total de Views")
    plt.ylabel("Views")
    plt.title("Total de Views por Banda")
    plt.show()
    
def print_instrumentalidade(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Instrumentalness'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="Orange")
    plt.xlabel("Total de Instrumentalidade")
    plt.ylabel("Instrumentalidade")
    plt.title("Total de Instrumentalidade por Banda")
    plt.show()
    
def print_valencia(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Valence'].sum() for banda in bandas]

    plt.figure(figsize=(10,6))
    plt.bar(nomes, likes_totais, color="Purple")
    plt.xlabel("Total de Valência")
    plt.ylabel("Valência")
    plt.title("Total de Valência por Banda")
    plt.show()

def teste(bandas):
    for banda, dados in bandas:
        sns.lmplot(x='Likes', y='Views', data=dados, fit_reg=True, hue='Artist')
        plt.title(f"Relação entre Likes e Views para {banda}")
        plt.show()