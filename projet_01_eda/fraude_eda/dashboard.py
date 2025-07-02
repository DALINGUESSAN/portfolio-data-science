import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🔍 Dashboard – Détection de Fraude Bancaire")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\hp\Downloads\projet data analyste\creditcard.csv')

df = load_data()

# Aperçu du dataset
st.subheader("Aperçu des données")
st.dataframe(df.head())

# Distribution de la variable cible
st.subheader("Distribution des classes (Fraude = 1, Normal = 0)")
fig1, ax1 = plt.subplots()
sns.countplot(x="Class", data=df, ax=ax1)
st.pyplot(fig1)

# Distribution des montants
st.subheader("Distribution du montant des transactions")
fig2, ax2 = plt.subplots()
sns.histplot(df['Amount'], bins=100, kde=True, ax=ax2)
st.pyplot(fig2)

# Boxplot montant vs fraude
st.subheader("Montant selon le type de transaction")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Class', y='Amount', data=df, ax=ax3)
st.pyplot(fig3)

# Heatmap de corrélations
st.subheader("Matrice de corrélation")
fig4, ax4 = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(), cmap='coolwarm', ax=ax4)
st.pyplot(fig4)