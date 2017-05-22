import pandas as pd

def line(df):

    year_count = df.groupby('Year').count().reset_index()
    year_count.Year = year_count.Year.astype('int')

    # remove data after 2015
    year_count = year_count[year_count.Year <= 2015]
    x = year_count.Year.tolist()
    y = year_count.Name.tolist()
    return (x,y)

def stack(df):
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

def scatter(df):
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


def bubble_chart(df):
    genre_list = sorted(list(df['Genre'].unique()))
    series = []

    for i in range(len(genre_list)):
        genre_series = {}
        genre_data = []
        
        df1 = df[df['Genre']==genre_list[i]][['Year','Global_Sales','Name','Publisher']]
        values = df1.values.tolist()
        for value in values:
            dict = {}
            dict['x']=value[0]
            dict['y']=value[1]
            dict['z']=value[1]
            dict['name']=value[2]
            dict['publisher']= value[3]
            dict['genre']=genre_list[i]
            genre_data.append(dict)
        genre_series['name']=genre_list[i]
        genre_series['data']=genre_data
        series.append(genre_series)
    return (series)    
