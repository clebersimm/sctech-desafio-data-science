import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# metódo responsável por carregar os dados de um arquivo CSV e retornar um DataFrame do pandas 
def carregar_arquivo_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{caminho_arquivo}' está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: O arquivo '{caminho_arquivo}' contém erros de formatação.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")

# Verifica e remove linhas duplicadas, mantendo apenas a última ocorrência
def remover_linhas_duplicadas(df):
    total_linhas_duplicadas = df.duplicated().sum()
    if total_linhas_duplicadas > 0:
        df.drop_duplicates(keep='last', inplace=True)
    return df

# Remove as colunas especificadas do DataFrame, passando como parâmetro uma lista de colunas
def remover_colunas_desnecessarias(df, colunas_para_remover):
    df.drop(columns=colunas_para_remover, inplace=True)

# Transforma os nomes das colunas de inglês para português
def ajustar_nomeclatura_colunas(df):
    df.rename(columns={
        'PassengerId':'identificacao_passageiro',
        'Survived':'sobreviveu',
        'Pclass':'classe',
        'Sex':'genero',
        'Name':'nome',
        'Age':'idade',
        'SibSp':'irmaos_conjuges',
        'Parch':'pais_filhos',
        'Ticket':'ticket',
        }, inplace=True)

def ajustar_valores(df):
    df['genero'] = df['genero'].map({'male': 'Masculino', 'female': 'Feminino'})
    df['idade'] = df['idade'].fillna(df['idade'].median())

# Função para salvar o gráfico em um diretório específico, criando o diretório se ele não existir
def gravar_arquivo(plt, nome_arquivo):
    diretorio_saida = "relatorios"
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    caminho_completo = os.path.join(diretorio_saida, nome_arquivo)
    plt.savefig(caminho_completo)

def plotar_histograma_idade(df, gerar_arquivo=False):
    plt.figure(figsize=(10, 6))
    sobreviventes_por_idade = df[df['sobreviveu'] == 1]['idade']
    plt.hist(sobreviventes_por_idade, bins=20, color='green', edgecolor='black')
    plt.title('Distribuição da idade dos sobreviventes')
    plt.xlabel('Idade')
    plt.ylabel('Número de sobreviventes')
    plt.grid(axis='y', linestyle='--',alpha=0.75)
    plt.tight_layout()
    if gerar_arquivo:
        gravar_arquivo(plt, 'histograma_idade_sobreviventes.png')
    else:
        plt.show()

def plotar_grafico_barra(df, parametros, gerar_arquivo=False):
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', color='blue', edgecolor='black')
    plt.title(parametros['titulo'])
    plt.xlabel(parametros['legenda_eixo_x'], rotation=0)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Quantidade')
    plt.grid(axis='y', linestyle='--', alpha=0.75)
    plt.legend(labels=parametros['totais'], loc='upper right', fontsize='small', frameon=True, shadow=True)
    plt.tight_layout()
    if gerar_arquivo:
        gravar_arquivo(plt, parametros['arquivo_saida'])
    else:
        plt.show()

def plotar_grafico_pizza(df, parametros, gerar_arquivo=False):
    plt.figure(figsize=(8, 8))
    df.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(parametros['titulo'])
    plt.tight_layout()
    if gerar_arquivo:
        gravar_arquivo(plt, parametros['arquivo_saida'])
    else:
        plt.show()

def sobreviventes_por_genero(df):
    total_genero_feminino = df[df['genero'] == 'Feminino'].shape[0]
    sobreviventes_genero_feminino = df[(df['genero'] == 'Feminino') & (df['sobreviveu'] == 1)].shape[0]

    # Plotar gráfico de barras para mulheres
    dados_mulheres = pd.Series({
        'Total embarcado': total_genero_feminino,
        'Sobreviventes': sobreviventes_genero_feminino
    })
    plotar_grafico_barra(dados_mulheres, {
        'titulo': 'Genero feminino: Total embarcado vs Sobreviventes',
        'legenda_eixo_x': 'Situação',
        'totais':'1',
        'arquivo_saida': 'genero_feminino_embarcadas_vs_sobreviventes.png'
    }, gerar_arquivo=True)


def agrupar_sobreviventes_por_familia(df):
    df['familia'] = df['nome'].apply(lambda x: x.split(',')[0])
    sobreviventes_por_familia = df.groupby(['familia','sobreviveu']).size().sort_values(ascending=False)
    print(sobreviventes_por_familia)

def main():
    df = carregar_arquivo_csv("data/titanic_dataset.csv")
    remover_colunas_desnecessarias(df, ['Fare', 'Cabin', 'Embarked'])
    remover_linhas_duplicadas(df)
    ajustar_nomeclatura_colunas(df)
    ajustar_valores(df)
    
    plotar_histograma_idade(df, gerar_arquivo=True)
    totais = f'Mulheres: {df.query('genero == "Feminino"').groupby('genero').size().iloc[0]} \n Homens:{df.query('genero == "Masculino"').groupby('genero').size().iloc[0]}'
    plotar_grafico_barra(df.groupby('genero').size(),{'titulo':'Total de passageiros por genero','legenda_eixo_x':'Gênero','totais':totais,'arquivo_saida':'total_passageiros_por_genero.png'}, gerar_arquivo=True)
    plotar_grafico_pizza(df.query('sobreviveu == 1').groupby('genero').size(),{'titulo':'Total de sobreviventes por genero','legenda_eixo_x':'Gênero','arquivo_saida':'total_sobreviventes_por_genero.png'}, gerar_arquivo=True)
    plotar_grafico_pizza(df.query('sobreviveu == 1').groupby(['genero', 'classe']).size(),{'titulo':'Total de sobreviventes por genero e classe','legenda_eixo_x':'Gênero/Classe','arquivo_saida':'total_sobreviventes_por_genero_e_classe.png'}, gerar_arquivo=True)
    plotar_grafico_barra(df.query('sobreviveu == 1 and idade <= 18').groupby('idade').size(),{'titulo':'Total de sobreviventes menores de 18 anos','legenda_eixo_x':'Idade','totais':'1','arquivo_saida':'total_sobreviventes_menores_de_18_anos.png'}, gerar_arquivo=True)
    plotar_grafico_barra(df.query('sobreviveu == 1 and idade <= 18 and pais_filhos == 0').groupby('idade').size(),{'titulo':'Total de sobreviventes menores de 18 anos sem pais','totais':'1','legenda_eixo_x':'Idade','arquivo_saida':'total_sobreviventes_menores_de_18_anos_sem_pais.png'}, gerar_arquivo=True)
    sobreviventes_por_genero(df)
    
    #agrupar_sobreviventes_por_familia(df)

if __name__ == "__main__":
    main()
