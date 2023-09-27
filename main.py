import pandas as pd
import graficos

def print_menu():
    print("+------------- MENU --------------+")
    print("| [1] Buscar uma banda            |")
    print("| [2] Comparar as bandas buscadas |")
    print("| [3] Mostrar estatísticas        |")
    print("| [4] Sair                        |")
    print("+---------------------------------+")

def print_menu_graficos():
    print("+-------------- MENU --------------+")
    print("| [1] Gráfico de Likes             |")
    print("| [2] Gráfico de Views             |")
    print("| [3] Gráfico de Instrumentalidade |")
    print("| [4] Gráfico de Valência          |")
    print("| [5] Relação entre Likes e Views  |")
    print("| [6] Sair                         |")
    print("+----------------------------------+")


caminho = "Spotify_Youtube.csv"

df = pd.read_csv(caminho, encoding="latin-1")
print(df.info())

bandas = []

while True:
    print_menu()
    try:
        op = int(input("Selecione uma das opções acima: "))
    except ValueError:
        continue

    match op:
        case 1:
            banda = input("Digite o nome da banda ou do artista (ou 'sair' para encerrar): ")
    
            df_banda = df[df['Artist'] == banda]

            if not df_banda.empty:
                df_res = df_banda.groupby(["Artist","Track","Views","Likes","Instrumentalness"])["Valence"].sum().reset_index()
                print(df_res)
                bandas.append((banda, df_res))
            else:
                print(f"Banda ou artista '{banda}' não encontrado.")
        case 2:
            for banda, df_res in bandas:
                print(f"Comparando dados para {banda}: ")
                print(df_res)
        case 3:
            while True:
                print_menu_graficos()
                try:
                    tipo_grafico = int(input("Selecione uma das opções acima: "))
                except ValueError:
                    continue
                match tipo_grafico:
                    case 1:
                        graficos.print_likes(bandas)
                    case 2:
                        graficos.print_views(bandas)
                    case 3:
                        graficos.print_instrumentalidade(bandas)
                    case 4:
                        graficos.print_valencia(bandas)
                    case 5:
                        graficos.relacao_likes_views(bandas)
                    case 6:
                        break    
                         
        case 4:
            break
        case _:
            print("Opção não encontrada...")
    


