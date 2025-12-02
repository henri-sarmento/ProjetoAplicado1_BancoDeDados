import pandas as pd
import matplotlib.pyplot as plt

# Ler CSV com separador correto
df = pd.read_csv(
    "desembolsos-mpme-por-subsetor-bndes-desembolsos-mpme.csv",
    sep=";"
)

# Limpar nomes das colunas
df.columns = df.columns.str.replace('"', '').str.strip()

# Garantir que 'ano' seja inteiro
df['ano'] = df['ano'].astype(int)

# Agrupar por ano somando todos os meses
df_ano = df.groupby("ano").sum(numeric_only=True)

# Remover colunas que não são subsetores
colunas_subsetores = [c for c in df_ano.columns if c != "mes"]

# Selecionar top 5 subsetores pelo total desembolsado
top_subsetores = df_ano[colunas_subsetores].sum().nlargest(5).index

# Plotar gráfico de linha
plt.figure(figsize=(12, 6))
for subsetor in top_subsetores:
    plt.plot(df_ano.index, df_ano[subsetor], marker='o', label=subsetor)

plt.title("Evolução dos Desembolsos do BNDES para MPMEs (Top 5 Subsetores)")
plt.xlabel("Ano")
plt.ylabel("Desembolso (R$)")
plt.legend(title="Subsetor", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
