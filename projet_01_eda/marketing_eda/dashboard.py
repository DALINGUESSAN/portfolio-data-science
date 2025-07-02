import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Dashboard – Campagne Marketing")

@st.cache_data
def load_data():
    return pd.read_csv("data/marketing_campaign.csv", sep=';')

df = load_data()

st.subheader("Aperçu du dataset")
st.dataframe(df.head())

st.subheader("Distribution des revenus")
fig1, ax1 = plt.subplots()
sns.histplot(df["Income"].dropna(), bins=50, kde=True, ax=ax1)
st.pyplot(fig1)

st.subheader("Réponse aux campagnes")
fig2, ax2 = plt.subplots()
sns.countplot(x="Response", data=df, ax=ax2)
st.pyplot(fig2)

st.subheader("Dépenses (Wine vs Gold)")
fig3, ax3 = plt.subplots()
sns.scatterplot(x="MntWines", y="MntGoldProds", hue="Response", data=df, ax=ax3)
st.pyplot(fig3)