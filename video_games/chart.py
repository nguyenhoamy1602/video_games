import pandas as pd

def chart1(df):

    year_count = df.groupby('Year').count().reset_index()
    year_count.Year = year_count.Year.astype('int')

    # remove data after 2015
    year_count = year_count[year_count.Year <= 2015]
    x = year_count.Year.tolist()
    y = year_count.Name.tolist()
    return (x,y)

def chart2(df):
    year_sale = df.groupby('Year')['NA_Sales','EU_Sales','JP_Sales','Other_Sales'].sum().reset_index().round(2)
    year_sale.Year = year_sale.Year.astype('int')
    # remove data after 2015
    year_sale = year_sale[year_sale.Year <= 2015]
    series = []
    data = year_sale.values.T.tolist()
    year = data[0]
    region = ['North America', 'Europe', 'Japan', 'Other']
    for i in range(len(region)):
        dict = {}
        dict['name']= region[i]
        dict['data']= data[i+1]
        series.append(dict)
    return (year, series)

def chart3(df):
    genre_list = sorted(list(df['Genre'].unique()))
    series = []
    for i in range(len(genre_list)):
        dict = {}
        df1 = df[df['Genre']==genre_list[i]][['Global_Sales','Name']]
        sales_names = df1.values.tolist()
        for u in range(len(sales_names)):
            sales_names[u].insert(0,i)
        dict['data']=sales_names
        series.append(dict)
    return (genre_list, series)
