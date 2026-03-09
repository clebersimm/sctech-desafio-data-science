import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def carregar_arquivo_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        #print(f"Arquivo '{caminho_arquivo}' carregado com sucesso!")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{caminho_arquivo}' está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: O arquivo '{caminho_arquivo}' contém erros de formatação.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")

def remover_linhas_duplicadas(df):
    #print(f"Verificando linhas duplicadas. Total de linhas antes da limpeza: {len(df)}")
    total_linhas_duplicadas = df.duplicated().sum()
    #print(f"Total de linhas duplicadas encontradas: {total_linhas_duplicadas}")
    if total_linhas_duplicadas > 0:
        df.drop_duplicates(keep='last', inplace=True)
     #   print(f"Linhas duplicadas removidas. Total de linhas após limpeza: {len(df)}")
    return df

def remover_colunas_desnecessarias(df, colunas_para_remover):
    #print(f"Removendo colunas desnecessárias: {colunas_para_remover}")
    df.drop(columns=colunas_para_remover, inplace=True)

def ajustar_nomeclatura_colunas(df):
    #print("Ajustando a nomenclatura das colunas para português...")
    df.rename(columns={
        'PassengerId':'identificacao_passageiro',
        'Survived':'sobreviveu',
        'Pclass':'classe',
        'Sex':'genero',
        'Name':'nome',
        'Age':'idade',
        'SibSp':'irmaos_conjuges',
        'Parch':'pais_filhos',
        'Ticket':'bilhete',
        'Fare':'tarifa',
        'Cabin':'cabine',
        'Embarked':'porto_de_embarque'
        }, inplace=True)

def ajustar_valores(df):
    df.replace(np.nan, '-1', inplace=True)
    df.replace('male', 'Masculino', inplace=True)
    df.replace('female', 'Feminino', inplace=True)

def gravar_arquivo(plt, nome_arquivo):
    diretorio_saida = "relatorios"
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    caminho_completo = os.path.join(diretorio_saida, nome_arquivo)
    plt.savefig(caminho_completo)


def plotar_grafico_barra(dados_processados, dados_plotar_grafico, gerar_arquivo=False):
    plt.figure(figsize=(10, 6))
    dados_processados.plot(kind='bar', )
    plt.title(dados_plotar_grafico['titulo'])
    plt.xlabel(dados_plotar_grafico['legenda_eixo_x'])
    plt.xticks(rotation=45)
    plt.ylabel('Total')
    if gerar_arquivo:
        gravar_arquivo(plt, dados_plotar_grafico['arquivo_saida'])
    else:
        plt.show()

def main():
    df = carregar_arquivo_csv("data/titanic_dataset.csv")
    remover_colunas_desnecessarias(df, ['Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    remover_linhas_duplicadas(df)
    ajustar_valores(df)
    ajustar_nomeclatura_colunas(df)
    
    #plotar_grafico_barra(df.groupby('genero').size(),{'titulo':'Total de passageiros por genero','legenda_eixo_x':'Gênero','arquivo_saida':'total_passageiros_por_genero.png'}, gerar_arquivo=False)
    #plotar_grafico_barra(df.query('sobreviveu == 1').groupby('genero').size(),{'titulo':'Total de sobreviventes por genero','legenda_eixo_x':'Gênero','arquivo_saida':'total_sobreviventes_por_genero.png'}, gerar_arquivo=False)
    #plotar_grafico_barra(df.query('sobreviveu == 1').groupby(['genero', 'classe']).size(),{'titulo':'Total de sobreviventes por genero por classe','legenda_eixo_x':'Gênero','arquivo_saida':'total_sobreviventes_por_genero.png'}, gerar_arquivo=False)

"""
    # Cálculo dos dados para mulheres
    total_feminino = df[df['genero'] == 'Feminino'].shape[0]
    sobreviventes_feminino = df[(df['genero'] == 'Feminino') & (df['sobreviveu'] == 1)].shape[0]
    percentual_sobreviventes = (sobreviventes_feminino / total_feminino) * 100 if total_feminino > 0 else 0

    print(f"Total de mulheres que embarcaram: {total_feminino}")
    print(f"Total de mulheres que sobreviveram: {sobreviventes_feminino}")
    print(f"Percentual de mulheres sobreviventes: {percentual_sobreviventes:.2f}%")

    # Plotar gráfico de barras para mulheres
    import pandas as pd
    dados_mulheres = pd.Series({
        'Total embarcado': total_feminino,
        'Sobreviventes': sobreviventes_feminino
    })
    plotar_grafico_barra(dados_mulheres, {
        'titulo': 'Mulheres: Total embarcado vs Sobreviventes',
        'legenda_eixo_x': 'Situação',
        'arquivo_saida': 'mulheres_embarcadas_vs_sobreviventes.png'
    }, gerar_arquivo=False)
"""

if __name__ == "__main__":
    main()
