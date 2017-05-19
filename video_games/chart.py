from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import StringIO
import base64
import seaborn as sns

def chart1(df):

    img = StringIO.StringIO()

    platGenre = pd.crosstab(df.Platform, df.Genre)
    platGenreTotal = platGenre.sum(axis=1).sort_values(ascending = False)
    plt.figure(figsize=(8,6))
    sns.barplot(y = platGenreTotal.index, x = platGenreTotal.values, orient = 'h')
    plt.ylabel = "Platform"
    plt.xlabel = "The amount of games"
    
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())

    return plot_url

def chart2(df):
    table = pd.pivot_table(df, values='Global_Sales')
    img = StringIO.StringIO()

    platGenre = pd.crosstab(df.Platform, df.Genre)
    platGenreTotal = platGenre.sum(axis=1).sort_values(ascending = False)
    plt.figure(figsize=(8,6))
    sns.barplot(y = platGenreTotal.index, x = platGenreTotal.values, orient = 'h')
    plt.ylabel = "Platform"
    plt.xlabel = "The amount of games"
    
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())

    return plot_url

