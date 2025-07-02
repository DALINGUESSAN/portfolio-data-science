import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_conversion_rates(df, group_col='group', outcome_col='converted'):
    rates = df.groupby(group_col)[outcome_col].mean().reset_index()
    sns.barplot(x=group_col, y=outcome_col, data=rates)
    plt.title('Taux de conversion par groupe')
    plt.ylabel('Taux de conversion')
    plt.xlabel('Groupe')
    plt.ylim(0, 1)
    plt.show()
