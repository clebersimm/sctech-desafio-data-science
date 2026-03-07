# Desafio extra Introdução ao data science

SCtech.

## Objetivo do projeto  

```
O estudante deverá utilizar a base de dados pública do Titanic, em formato CSV, com o
objetivo de realizar uma Análise Exploratória de Dados (AED). A atividade consiste em
importar, organizar e analisar o conjunto de dados, buscando compreender o
comportamento geral das informações e identificar padrões, relações entre variáveis e
possíveis fatores associados à sobrevivência dos passageiros. A partir desse processo,
espera-se a obtenção de insights relevantes, como estatísticas descritivas, distribuições,
comparações entre grupos e análises exploratórias das variáveis disponíveis.
```

## Dicionário de dados  

|Coluna|Descrição|Tipo|
|---|---|---|
|PassengerId||Numérico|
|Survived||Numerico 0/1|
|Pclass||Numerico|
|Name|Nome dos passageiros|texto|
|Sex||text male/female|
|Age||numerico|
|SibSp||numerico|
|Parch||numerico|
|Ticket||texto|
|Fare||dinheiro|
|Cabin||texto|
|Embarked||texto|

## Ferramentas utilizadas

- vscode
  - Extensões: github copilot, markdown preview, pylance, python, python debugger, python environments
- python: python3.12.3

## Desenvolvimento do projeto  

- Instalação do [uv](https://docs.astral.sh/uv/) para gerenciamento de pacotes, ambientes virtuais e execução do projeto. O projeto uv foi desenvolvido para trazer mais performance nas atividades de desenvolvimento dos projetos em python.
- Iniciar novo projeto: **uv init sctech-desafio-data-science**.
- Todas as atividades são executas na pasta sctech-desafio-data-science
- Criar nova pasta para armazenamento de dados, desta forma mantendo separação dos arquivos e fonte de dados(arquivos).
- Instalar o pandas: uv add pandas

## Executar o projeto   

no terminal, na pasta sctech-desafio-data-science, executar uv run main.py