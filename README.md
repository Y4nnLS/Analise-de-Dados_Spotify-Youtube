<h1 align='center'>
    <img src="./assets/img1.png">
    <p>Analise de Dados - Spotify_Youtube</p>
</h1>

## Indice
- [Sobre](#📘-sobre)
- [Membros](#🙋‍♂️-equipe-de-desenvolvedores)
- [Ferramentas](#📝-ferramentas)
- [comandos](#comandos)
- [Acesso a base de dados](#📁-acesso-ao-dataset)

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

#### Funções Principais:
- `print_menu()` : Exibe um menu de opções para o usuário.
- `print_menu_graficos()`: Exibe um menu de opções para escolher o tipo de gráfico a ser exibido.
- `print_likes(bandas)`: Gera um gráfico de barras mostrando o total de 'likes' para cada banda.
- `print_views(bandas)`: Gera um gráfico de barras mostrando o total de 'views' para cada banda.
- `print_instrumentalidade(bandas)`: Gera um gráfico de barras mostrando a soma da 'instrumentalidade' para cada banda.
- `print_valencia(bandas)`: Gera um gráfico de barras mostrando a soma da 'valência' para cada banda.
- `teste(bandas)`: Gera gráficos de dispersão mostrando a relação entre 'Likes' e 'Views' para cada banda.

#### Análises Permitidas:

- Busca de uma Banda ou Artista: O usuário pode inserir o nome de uma banda ou artista para encontrar dados relacionados a ela no conjunto de dados.
- Comparação de Bandas: O programa permite ao usuário comparar os dados das bandas que foram buscadas anteriormente.
- Visualização de Estatísticas: O programa oferece a possibilidade de visualizar estatísticas por meio de gráficos para as bandas encontradas.

#### Interação com o Programa:

- O programa interage com o usuário por meio do console/terminal, exibindo menus com opções numeradas.
- O usuário pode selecionar uma opção digitando o número correspondente e pressionando Enter.

#### Gráficos que podem ser gerados:

- Gráfico de Likes: Um gráfico de barras que mostra o total de `likes` para cada banda.
- Gráfico de Views: Um gráfico de barras que mostra o total de `views` para cada banda.
- Gráfico de Instrumentalidade: Um gráfico de barras que mostra a soma da `instrumentalidade` para cada banda.
- Gráfico de Valência: Um gráfico de barras que mostra a soma da `valência` para cada banda.
- Gráfico de Dispersão - Relação entre `Likes` e `Views` por Banda.

## 📝 Ferramentas

- [Python](https://docs.python.org/3/)
- [Pandas](https://pandas.pydata.org/docs/)
- [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [seaborn](https://seaborn.pydata.org)

## Comandos

<p> instala todas as dependências listadas em requirements.txt :</p>

    pip install -r requirements.txt    

<p> lista os modulos disponíveis : </p> 

    pip list 


## 📁 Acesso ao DataSet

-  [<img src="./assets/google-drive-logo.png" height="15" width="15"> Google Drive](https://drive.google.com/drive/folders/1fiu2pjUhPKP6_6GgjglLsAjOP9Anu_Ce?usp=drive_link)
- [<img src="./assets/Kaggle_logo.png" height="20">](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube/data)