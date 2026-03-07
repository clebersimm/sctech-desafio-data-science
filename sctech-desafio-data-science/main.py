import pandas as pd
import numpy as np

def carregar_arquivo_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"Arquivo '{caminho_arquivo}' carregado com sucesso!")
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
    print(f"Verificando linhas duplicadas. Total de linhas antes da limpeza: {len(df)}")
    total_linhas_duplicadas = df.duplicated().sum()
    print(f"Total de linhas duplicadas encontradas: {total_linhas_duplicadas}")
    if total_linhas_duplicadas > 0:
        df.drop_duplicates(keep='last', inplace=True)
        print(f"Linhas duplicadas removidas. Total de linhas após limpeza: {len(df)}")
    return df

def ajustar_nomeclatura_colunas(df):
    print("Ajustando a nomenclatura das colunas para português...")
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
        'Embarked':'embarque'
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
    contagem['relacao_sobrevivencia'] = contagem['sobreviventes'] / contagem['total_passageiros']
    return contagem

def main():
    df = carregar_arquivo_csv("data/titanic_dataset.csv")
    remover_linhas_duplicadas(df)
    ajustar_nomeclatura_colunas(df)
    ajustar_valores_nulos(df)
    dados_processados = {
        'relacao_sobrevivencia_por_classe': relacao_sobrevivencia_por_colunas(df, ['classe']),
        'relacao_sobrevivencia_por_genero': relacao_sobrevivencia_por_colunas(df, ['genero']),
        'relacao_sobrevivencia_por_genero_classe': relacao_sobrevivencia_por_colunas(df, ['genero', 'classe'])
    }
    print(dados_processados)


if __name__ == "__main__":
    main()
