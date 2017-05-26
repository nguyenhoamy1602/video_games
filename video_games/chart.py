# Functions to get data for Highcharts
import pandas as pd
from scipy import stats

aggFunc = ['count', 'sum', 'mean']
categories = ["Genre", "Publisher", "Platform", "Year"]

def category_data(df, category):
    """Get Global Sales count, sum and mean according to Year into a list"""
    data = df.groupby(category).agg({'Global_Sales': aggFunc}).round(2)

    # turn data into list
    dataset = data.values.T.tolist()
    dataset.insert(0, data.index.tolist())
    return dataset

def aggregate(df, category):
    """Get Global Sales count, sum and mean 
    according to category other than year and form a dict"""
    data = df.groupby(category).agg({'Global_Sales': aggFunc}).round(2)
    
    category_list = data.index.tolist()
    values = data.values.tolist()

    # add data to dictionary
    data_dict = {}
    for i in range(len(category_list)):
        data_dict[category_list[i]] = values[i]
    return data, data_dict

def top_performer(df, category):
    """Get top 10 performer in mean, sum and count, 
    then create a unique list"""

    data, data_dict = aggregate(df, category)
    top_category = []

    # get top 10 for each category
    for i in aggFunc:
        top10 = data["Global_Sales"][i].sort_values(ascending=False).head(10)
        top_category.append(top10.index.tolist())

    # create a unique list of top performer   
    top_perform = [item for sublist in top_category for item in sublist]
    top_perform = sorted(list(set(top_perform)))

    # create a list of dataset for top performer
    dataset = []
    for i in top_perform:
        dataset.append(data_dict[i])
    dataset = [list(x) for x in zip(*dataset)]
    dataset.insert(0,top_perform)
    return top_perform, dataset

def combined(df):
    """Combine all datas together for mixed chart"""
    combined_data = {}
    for i in categories:
        if i == 'Year':
            combined_data['Year'] = category_data(df, i)
        else:
            dataset = top_performer(df, i)[1]
            combined_data[i] = dataset
    return combined_data 

def scatter_regress(df):
    data = {}
    for i in categories:
        data[i] = category_data(df, i)
        regress = stats.mstats.linregress(data[i][1], data[i][2])
        m = regress[0]
        c = regress[1]
        data[i] = [list(a) for a in zip(data[i][1], data[i][2],data[i][0])]
        mini = min(data[i])
        maxi = max(data[i])
        regress_data = []
        for u in [mini,maxi]:        
            regress_data.append([u[0],m*u[0]+c])
        data[i] = [regress_data,data[i]]
    return data



def area(df):
    """Get data for area chart - regional sales"""
    year_sale = df.groupby('Year')['Global_Sales','NA_Sales',
    'EU_Sales','JP_Sales','Other_Sales'].sum().reset_index().round(2)
    year_sale.Year = year_sale.Year.astype('int')

    # remove data after 2015
    year_sale = year_sale[year_sale.Year <= 2015]
    series = []
    data = year_sale.values.T.tolist()
    year = data[0]
    region = ['Global', 'North America', 'Europe', 'Japan', 'Other']

    # update data for each region in a dictionary
    for i in range(len(region)):
        dict = {}
        dict['name']= region[i]
        dict['data']= data[i+1]
        series.append(dict)
    return (year, series)

def scatter(df,category):
    """Get data for scatter chart - Global Sales according to Category"""
    top_perform = top_performer(df, category)[0]
    series = []
    for i in range(len(top_perform)):
        dict = {}
        df1 = df[df[category]==top_perform[i]][['Global_Sales','Name']]
        sales_names = df1.values.tolist()
        for u in range(len(sales_names)):
            sales_names[u].insert(0,i)
        dict['data']=sales_names
        series.append(dict)   
    return top_perform, series

def scatter_data(df):
    scatter_data = {}
    for i in categories:
        scatter_data[i] = list(scatter(df, i))
    return scatter_data


def bubble_chart(df):
    """Get data according to Genre """
    genre_list = sorted(list(df['Genre'].unique()))
    series = []

    for i in range(len(genre_list)):
        # create a dictionary for each genre
        genre_series = {}
        genre_data = []
        
        # get data and add to dictionary
        df1 = df[df['Genre']==genre_list[i]][['Year','Global_Sales',
        'Name','Publisher']]
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
