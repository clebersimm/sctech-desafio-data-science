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
|PassengerId|Identificação do passageiro|Numérico|
|Survived|1 - sobreviveu, 0 - não sobreviveu|Numerico 0/1|
|Pclass|1- primeira(convés superior), 2- segunda(meio), 3- terceira(convés inferior)|Numerico|
|Name|Nome dos passageiros|texto|
|Sex|genero|text male/female|
|Age|Idade|numerico|
|SibSp|Irmãos/conjuges|numerico|
|Parch|pais/filhos|numerico|
|Ticket|bilhete|texto|
|Fare|tarifa|dinheiro|
|Cabin|cabine|texto|
|Embarked|porto de embarque|texto|

## Ferramentas utilizadas

- vscode
  - Extensões: github copilot, markdown preview, pylance, python, python debugger, python environments
- python: python3.12.3
  - libs: pandas, matplotlib

## Desenvolvimento do projeto  

- Instalação do [uv](https://docs.astral.sh/uv/) para gerenciamento de pacotes, ambientes virtuais e execução do projeto. O projeto uv foi desenvolvido para trazer mais performance nas atividades de desenvolvimento dos projetos em python.
- Iniciar novo projeto: **uv init sctech-desafio-data-science**.
- Todas as atividades são executas na pasta sctech-desafio-data-science
- Criar nova pasta para armazenamento de dados, desta forma mantendo separação dos arquivos e fonte de dados(arquivos).
- Instalar o pandas: uv add pandas
- Instalar matplot: uv add matplotlib
- Dividido por métodos as funcionalidades para melhor leitura do código e no caso de algum bug mais fácil de identificar.
- Criado método para gerar os gráficos mais utilizados e outro método para gerar as imagens para dentro do diretório de relatórios.
- No método de ajustar_valores foi escolhido colocar a medianda da idade para manter a quantidade de valores. Esta decisão foi tomada depois de pesquisar se era melhor remover ou colocar a mediana, pela pesquisa foi exposto que para análise estatística é melhor manter a mediana.

## Executar o projeto   

no terminal, na pasta sctech-desafio-data-science, executar uv run main.py


## Desenvolvimento da solução   

Para o desenvolvimento do projeto exposto, verificação de dados que possam ter sido relevantes para a sobrevivencia dos passageiros do Titanic, foram verificados dados como:
- Genero
- Idade
- Classe social  




Foram desenvolvidos os relatórios de histógrama de sobreviventes pela idade.   

![Histograma de passageiros pela idade](./sctech-desafio-data-science/relatorios/histograma_idade_passageiros.png)

![Histograma de sobreviventes pela idade](./sctech-desafio-data-science/relatorios/histograma_idade_sobreviventes.png)


Total de passageiros por genero.   

![Total de passageiros por genero](./sctech-desafio-data-science/relatorios/total_passageiros_por_genero.png)   

Total de sobreviventes por genero.   

![Total de sobreviventes por genero](./sctech-desafio-data-science/relatorios/total_sobreviventes_por_genero.png)   


Total sobreviventes por genero e classe.    

![Total de sobreviventes por genero e classe](./sctech-desafio-data-science/relatorios/total_sobreviventes_por_genero_e_classe.png)