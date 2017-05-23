import pandas as pd

aggFunc = ['count', 'sum', 'mean']
categories = ["Genre", "Publisher", "Platform"]

def year_data(df):
    data = df.groupby("Year").agg({'Global_Sales': aggFunc}).round(2)
    dataset = data.values.T.tolist()
    dataset.insert(0, data.index.tolist())
    return dataset

def aggregate(df, category):
    data = df.groupby(category).agg({'Global_Sales': aggFunc}).round(2)
    data_dict = {}
    category_list = data.index.tolist()
    values = data.values.tolist()
    for i in range(len(category_list)):
        data_dict[category_list[i]] = values[i]
    return data, data_dict

def top_performer(df, category):
    data, data_dict = aggregate(df, category)
    top_category = []
    for i in aggFunc:
        top10 = data["Global_Sales"][i].sort_values(ascending=False).head(10)
        top_category.append(top10.index.tolist())
    top_perform = [item for sublist in top_category for item in sublist]
    top_perform = sorted(list(set(top_perform)))
    dataset = []
    for i in top_perform:
        dataset.append(data_dict[i])
    dataset = map(list, zip(*dataset))
    dataset.insert(0,top_perform)
    return top_perform, dataset

def combined(df):
    combined_data = {}
    combined_data['Year'] = year_data(df)
    for i in categories:
        dataset = top_performer(df, i)[1]
        combined_data[i] = dataset
    return combined_data 

def stack(df):
    year_sale = df.groupby('Year')['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales'].sum().reset_index().round(2)
    year_sale.Year = year_sale.Year.astype('int')
    # remove data after 2015
    year_sale = year_sale[year_sale.Year <= 2015]
    series = []
    data = year_sale.values.T.tolist()
    year = data[0]
    region = ['Global', 'North America', 'Europe', 'Japan', 'Other']
    for i in range(len(region)):
        dict = {}
        dict['name']= region[i]
        dict['data']= data[i+1]
        series.append(dict)
    return (year, series)

def scatter(df,category):
    top_perform = top_performer(df, category)[0]
    series = [top_perform]
    for i in range(len(top_perform)):
        dict = {}
        df1 = df[df[category]==top_perform[i]][['Global_Sales','Name']]
        sales_names = df1.values.tolist()
        for u in range(len(sales_names)):
            sales_names[u].insert(0,i)
        dict['data']=sales_names
        series.append(dict)    
    return series

def scatter_data(df):
    scatter_data = {}
    for i in categories:
        scatter_data[i] = scatter(df, i)
    return scatter_data




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
