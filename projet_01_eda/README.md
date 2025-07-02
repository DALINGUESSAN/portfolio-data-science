# Projet 01 Eda

Description du projet.

#  Portfolio Data Science – EDA Projects

Bienvenue dans mon portfolio de projets d'Analyse Exploratoire de Données (EDA) réalisé dans le cadre de ma formation Data Analyst / Data Scientist.

##  Outils & Technologies
- `Python`, `Pandas`, `NumPy`
- `Seaborn`, `Matplotlib`, `Plotly`
- `Jupyter Notebook`, `Streamlit`
- `Git`, `GitHub`

---

##  Contenu du projet

### 1.  Détection de Fraude Bancaire – *Credit Card Fraud*
- Analyse exploratoire des transactions.
- Traitement des variables déséquilibrées.
- Visualisations clés : heatmaps, distributions, corrélations.
-  Dossier : `fraude_eda/`
-  Dashboard interactif : `fraude_eda/dashboard.py`

#  Détection de Fraude – Credit Card Fraud

Ce projet analyse un jeu de données anonymisé de transactions bancaires afin de détecter les schémas caractéristiques de la fraude.

##  Objectifs
- Identifier les caractéristiques discriminantes des fraudes.
- Visualiser les corrélations et distributions selon le type de transaction.
- Préparer les données pour une modélisation future.

##  Visualisations clés
- Heatmap de corrélation
- Distribution des montants
- Comparaison des distributions entre transactions frauduleuses et non frauduleuses

##  Fichiers importants
- `fraude_eda/eda_fraude.py` → Script principal
- `fraude_eda/dashboard.py` → Interface Streamlit
- `fraude_eda/figures/` → Graphiques générés





# 2.  Segmentation Marketing – *Campaign Data*
- Analyse des campagnes de marketing relationnel.
- Segmentation RFM (Recency, Frequency, Monetary).
- Analyse des comportements d’achat.
-  Dossier : `marketing_eda/`
- 🖥 Dashboard interactif : `marketing_eda/dashboard.py`






#  2. `marketing_eda/README.md` — Analyse Marketing Campagne


#  Analyse Marketing – Campagne Relationnelle

Ce projet explore une base de données client d’une entreprise de vente en ligne pour analyser les comportements de consommation et la réponse à des campagnes.

##  Objectifs
- Identifier les profils les plus susceptibles de répondre à une campagne.
- Étudier les variables influentes : revenu, âge, dépenses, etc.
- Réduire la dimensionnalité avec la PCA.

##  Graphiques générés
| Graphique | Description |
|----------|-------------|
| Répartition des réponses | Clients ayant répondu (ou non) à la campagne |
| Distribution de l'âge | Calculée à partir de Year_Birth |
| Distribution des revenus | Outliers détectés |
| Dépenses par catégorie | Vins, produits d’or, fruits |
| Corrélations | Variables numériques uniquement |
| PCA | Visualisation 2D des clients selon leurs dépenses |

📁 Graphiques disponibles dans `marketing_eda/figures/`
##  Lancer l'analyse
```bash
cd fraude_eda/
python eda_fraude.py
# ou
streamlit run dashboard.py
##  Exécution locale
```bash
cd marketing_eda/
python eda_marketing.py
# ou
streamlit run dashboard.py



---

##  Lancer les projets localement

1. Cloner le dépôt :
```bash
git clone https://github.com/DALINGUESSAN/portfolio-EDA.git
2.Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Lancer un des dashboards :

bash
Copier le code
streamlit run fraude_eda/dashboard.py
# ou
streamlit run marketing_eda/dashboard.py
✍️ Auteur
Dalinguessan
📧 dalinguessan88@gmail.com
🔗 Mon LinkedIn (à adapter si tu veux)

 Objectif
Ce projet a pour but de démontrer mes compétences pratiques en :

Nettoyage et préparation des données

Visualisation statistique

Dashboarding interactif avec Streamlit

⭐ Si vous aimez ce projet, n’hésitez pas à le starrer !
