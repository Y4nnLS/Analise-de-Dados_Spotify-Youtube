<h1 align='center'>
    <img src="./assets/img1.png">
    <p>Analise de Dados - Spotify_Youtube</p>
</h1>

## Indice
- [Sobre](#📘-sobre)
- [Membros](#🙋‍♂️-equipe-de-desenvolvedores)
- [Ferramentas](#📝-ferramentas)
- [comandos](#comandos)
- [Acesso a base de dados](#📁-acesso-a-base-de-dados)

## 🙋‍♂️ Equipe de desenvolvedores
<p>Felipe Franco Pinheiro</p>
<p>Yann Lucas Saito da Luz</p>

## 📘 Sobre

Este é um programa que interage com o usuário para analisar e visualizar dados de bandas musicais.

Requerimentos:
    - pandas
    - graficos (módulo contendo funções para gerar gráficos)

#### Uso:
    1. O programa lê um arquivo CSV chamado "Spotify_Youtube.csv" contendo a base de dados de bandas.
    2. Permite ao usuário buscar bandas, comparar dados e visualizar estatísticas.

Funções Principais:
- 
- `print_menu()` : Exibe um menu de opções para o usuário.
- `print_menu_graficos()`: Exibe um menu de opções para escolher o tipo de gráfico a ser exibido.
- `print_likes(bandas)`: Gera um gráfico de barras mostrando o total de 'likes' para cada banda.
- `print_views(bandas)`: Gera um gráfico de barras mostrando o total de 'views' para cada banda.
- `print_instrumentalidade(bandas): Gera um gráfico de barras mostrando a soma da 'instrumentalidade' para cada banda.
- `print_valencia(bandas)`: Gera um gráfico de barras mostrando a soma da 'valência' para cada banda.
- `teste(bandas)`: Gera gráficos de dispersão mostrando a relação entre 'Likes' e 'Views' para cada banda.


## 📝 Ferramentas
- [Python](https://docs.python.org/3/)
- [Pandas](https://pandas.pydata.org/docs/)
- [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [seaborn](https://seaborn.pydata.org)

## Comandos

```bash
# instala todas as dependências listadas em arquivo .txt
    pip install -r requirements.txt    
```
```bash
# lista os modulos disponíveis      
    pip list 
```

## 📁 Acesso ao DataSet

-  [<img src="./assets/google-drive-logo.png" height="15" width="15"> Google Drive](https://drive.google.com/drive/folders/1fiu2pjUhPKP6_6GgjglLsAjOP9Anu_Ce?usp=drive_link)
- [<img src="./assets/Kaggle_logo.png" height="20">](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube/data)