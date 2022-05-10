# !pip install seaborn==0.9.0
# import seaborn as sns
# print(sns.__version__)

# Analisando notas em geral
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

notas = pd.read_csv("ratings.csv")
notas.head()

notas.shape

notas.columns = ("usuárioID", "FilmeID", "Nota", "Momento")
notas.head()

notas['Nota']

notas['Nota'].unique()

notas['Nota'].value_counts()

print(notas['Nota'].mean())
print(notas['Nota'].median())

notas.Nota.head()

notas.nota.plot()

notas.Nota.plot(kind="hist")

notas.Nota.describe()

sns.boxplot(notas.Nota)

plt.figure(figsize=(5,7))
sns.boxplot(y=notas.Nota)

# Olhando os filmes

filmes = pd.read_csv("movies.csv")
filmes.columns = ("filmeID", "titulo", "genero")
filmes.head()

notas.head()

# Analisando a média de Toy Story

notas.query("Filme == 1").Nota.mean()
notas.groupby("FilmeID")
notas.groupby("FilmeID").mean()

mediaFilmes = notas.groupby("FilmeID").mean().Nota
mediaFilmes.head()

mediaFilmes.plot(kind='hist')

sns.boxplot(mediaFilmes)

mediaFilmes.describe()

# Utilizando Seaborn para Gráfico de Histograma

sns.distplot(mediaFilmes)

# Histograma com pyplot

plt.hist(mediaFilmes)

plt.hist(mediaFilmes)
plt.title("Histograma das médias dos filmes")

plt.figure(figsize=(5,7))
sns.boxplot(y=mediaFilmes)

tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

tmdb.original_language.unique() #Categórica nominal

# Primeiro grau
# Segundo grau
# Terceiro grau
# 1º grau > 2º grau > 3º grau # Categórica Ordinal

#Budget => Orçamento => Quantitativa contínuo

# Indexando as línguas / organizando quantas vezes a língua se repete /
# Colocando em um bloco Língua | Quantidade / bloco enumerado
tmdb["original_language"].value_counts().index
tmdb["original_language"].value_counts().values
tmdb["original_language"].value_counts()
tmdb["original_language"].value_counts().to_frame()
tmdb["original_language"].value_counts().to_frame().reset_index()

contagem_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_lingua.columns = ["original_languages", "total"]
contagem_lingua.head()

sns.barplot(x="original_languages", y="total", data = contagem_lingua)
sns.catplot(x="original_language", kind="count", data=tmdb)

# Gráfico de pizza (Não recomendado o uso)

plt.pie(contagem_lingua["total"], labels = contagem_lingua["original_languages"])

# Separando lingua original dos filmes
total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_ingles = total_por_lingua.loc("en")
total_resto = total_geral - total_ingles
print(total_ingles, total_resto)

# Colocando a separação de linguas em um bloco
dados = {
    'lingua' : ['ingles', 'outros']
    'total' : [total_ingles, total_resto]
}
dados = pd.DataFrame(dados)
dados

sns.barplot(x="lingua", y="total", data = dados)

plt.pie(dados["total"], labels = dados["lingua"])

# Tirando a lingua inglesa do bloco de linguas
total_lingua_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
total_lingua_outros_filmes

filmes_lingua_nao_original = tmdb.query("original_language != 'en'")

sns.catplot(x="original_language", kind="count", data=filmes_lingua_nao_original)

# Arrumando a dimensão do gráfico

sns.catplot(x="original_language", kind="count", data=filmes_lingua_nao_original,
            aspect=3,
            palette="GnBu_d",
            order=total_lingua_outros_filmes.index)

filmes.head()
filmes.head(2)

notas_toy_story = notas.query("FilmeID==1")
notas_jumanji = notas.query("FilmeID==2")

print(len(notas_toy_story), len(notas_jumanji))

print("Nota média de Toy Story %.2f" % notas_toy_story.Nota.mean())
print("Nota média de Jumanji %.2f" % notas_jumanji.Nota.mean())

