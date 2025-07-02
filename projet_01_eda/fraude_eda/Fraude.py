import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
sns.set_palette('pastel')


df = pd.read_csv(r'C:\Users\hp\Downloads\projet data analyste\creditcard.csv')
df.head()

print("Dimensions du dataset :", df.shape)
print("\nTypes de variables :\n", df.dtypes)
print("\nValeurs manquantes :\n", df.isnull().sum().sort_values(ascending=False))
df.describe()

sns.countplot(x='Class', data=df)
plt.title('Répartition des classes (Fraude ou Non)')
plt.show()

fraud_ratio = df['Class'].mean()
print(f"Taux de fraude : {fraud_ratio:.4%}")

sns.histplot(df['Amount'], bins=100, kde=True)
plt.title("Distribution du montant des transactions")
plt.show()


sns.boxplot(x='Class', y='Amount', data=df)
plt.title("Montant selon le type de transaction")
plt.show()

corr = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap='coolwarm', linewidths=0.5)
plt.title("Matrice de corrélation")
plt.show()


grouped = df.groupby('Class')['Amount'].agg(['count', 'mean', 'std', 'min', 'max'])
print(grouped)


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = df.drop(columns=['Class', 'Time'])
y = df['Class']

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=y, palette='Set1', alpha=0.3)
plt.title("PCA – Visualisation des transactions")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()


