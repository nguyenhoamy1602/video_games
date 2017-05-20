from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import StringIO
import base64
import seaborn as sns



def chart1(df):

    year_count = df.groupby('Year').count().reset_index()
    year_count.Year = year_count.Year.astype('int')

    # remove data after 2016
    year_count = year_count[year_count.Year <= 2016]
    x = year_count.Year.tolist()
    y = year_count.Name.tolist()
    return (x,y)

def chart2(df):
    year_sale = df.groupby('Year')['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'].sum().reset_index().round(2)
    year_sale.Year = year_sale.Year.astype('int')
    # remove data after 2016
    year_sale = year_sale[year_sale.Year <= 2016]
    data = year_sale.values.T.tolist()
    return data

def chart3(df):

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
