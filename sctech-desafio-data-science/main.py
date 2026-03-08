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

def ajustar_valores_nulos(df):
    df.replace(np.nan, '-1', inplace=True)

def relacao_sobrevivencia_por_colunas(df, coluna):
    total_passageiros_por_coluna = df.groupby(coluna).size()
    sobreviventes_por_coluna = df.query("sobreviveu == 1").groupby(coluna).size()
    contagem = pd.DataFrame({
        'total_passageiros': total_passageiros_por_coluna,
        'sobreviventes': sobreviventes_por_coluna
    })
    contagem['relacao_sobrevivencia'] = (contagem['sobreviventes'] / contagem['total_passageiros']) * 100
    print(contagem)
    return contagem

def gravar_arquivo(plt, nome_arquivo):
    diretorio_saida = "relatorios"
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    caminho_completo = os.path.join(diretorio_saida, nome_arquivo)
    plt.savefig(caminho_completo)


def plotar_grafico_pizza(dados_processados, dados_plotar_grafico, gerar_arquivo=False):
    contagem = dados_processados[dados_plotar_grafico['indice']][dados_plotar_grafico['coluna']]
    plt.figure(figsize=(8, 8))
    plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140)
    plt.title(dados_plotar_grafico['titulo'])
    plt.axis('equal')
    plt.legend(title=dados_plotar_grafico['coluna'], loc='lower right')
    if gerar_arquivo:
        gravar_arquivo(plt, dados_plotar_grafico['arquivo_saida'])
    else:
        plt.show()
"""
def plotar_grafico_barra(dados_processados, dados_plotar_grafico, gerar_arquivo=False):
    contagem = dados_processados[dados_plotar_grafico['indice']][dados_plotar_grafico['coluna']]
    plt.figure(figsize=(10, 6))
    contagem.plot(kind='bar')
    plt.title(dados_plotar_grafico['titulo'])
    plt.xlabel(dados_plotar_grafico['legenda_eixo_x'])
    plt.ylabel('Total')
    plt.xticks(rotation=45)
    if gerar_arquivo:
        gravar_arquivo(plt, dados_plotar_grafico['arquivo_saida'])
    else:
        plt.show()
"""

def plotar_grafico_barra(dados_processados, dados_plotar_grafico, gerar_arquivo=False):
    plt.plot(dados_processados)
    plt.figure(figsize=(10, 6))
    dados_processados.plot(kind='bar')
    plt.title(dados_plotar_grafico['titulo'])
    plt.xlabel(dados_plotar_grafico['legenda_eixo_x'])
    plt.ylabel('Total')
    plt.xticks(rotation=45)
    if gerar_arquivo:
        gravar_arquivo(plt, dados_plotar_grafico['arquivo_saida'])
    else:
        plt.show()

def main():
    df = carregar_arquivo_csv("data/titanic_dataset.csv")
    remover_colunas_desnecessarias(df, ['Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    remover_linhas_duplicadas(df)
    ajustar_valores_nulos(df)
    ajustar_nomeclatura_colunas(df)
    total_passageiros = len(df)
    total_sobreviventes = df.query("sobreviveu == 1")['sobreviveu'].count()
    print(df.groupby('genero').size())
    dados_processados = {
        'total_passageiros': total_passageiros,
        'total_sobreviventes': total_sobreviventes,
        'relacao_sobrevivencia_por_classe': relacao_sobrevivencia_por_colunas(df, ['classe']),
        'relacao_sobrevivencia_por_genero': relacao_sobrevivencia_por_colunas(df, ['genero']),
        'relacao_sobrevivencia_por_genero_classe': relacao_sobrevivencia_por_colunas(df, ['genero', 'classe'])
    }
    
    #print(dados_processados)
    plotar_grafico_barra(dados_processados['relacao_sobrevivencia_por_genero'], {
        'indice': 'relacao_sobrevivencia_por_genero',
        'legenda_eixo_x': 'Gênero',
        'titulo': 'Relação de sobreviventes por gênero',
        'arquivo_saida': 'relacao_sobreviventes_por_genero.png'
    },gerar_arquivo=False)
    """
    plotar_grafico_pizza(dados_processados, {
        'indice': 'relacao_sobrevivencia_por_genero_classe',
        'coluna': 'sobreviventes',
        'titulo': 'Relação de sobreviventes por gênero e classe',
        'arquivo_saida': 'relacao_sobreviventes_por_genero_e_classe.png'
    },gerar_arquivo=False)
    """

if __name__ == "__main__":
    main()
