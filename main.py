# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:14:54 2017

@author: Melody Chai, My Ngyuen, Alex Sosin
"""

# Import all libraries needed for the tutorial
# Import all libraries needed for the tutorial
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import numpy as np
import csv

app = Flask(__name__)
iter_csv = pd.read_csv('Data/vgsales.csv', iterator=True, chunksize=1000)
df = pd.concat([chunk[chunk['Year'] >= 2000] for chunk in iter_csv])

aggFunctions = {'count':np.count_nonzero, 'sum':np.sum, 'avg':np.mean,
            'min':np.min, 'max':np.max, 'med':np.median}
filterLabels = {'NA_Sales':'North America Sales', 'EU_Sales': 'Europe Sales', 'JP_Sales': 'Japan Sales',
                   'Other_Sales': 'Other Sales', 'Global_Sales':'Global Sales'}
aggLabels = {'count': 'Counting', 'sum': 'Sum of', 'avg': 'Average of',
             'min': 'Minimum of', 'max': 'Maximum of', 'med': 'Median of'}


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/pivot', methods=['GET', 'POST'])
def pivot():
    if request.method == 'POST':
        cat1 = request.form['cat1']
        cat2 = request.form['cat2']
        aggr = request.form['aggr']
        filter = request.form['filter']
        if str(filter) == 'All':
            table = pd.pivot_table(df, index=[str(cat1), str(cat2)],
                                   values=["NA_Sales","EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"],
                                   aggfunc=aggFunctions[aggr], fill_value="")
        else:
            table = pd.pivot_table(df,index=[str(cat1)], columns=[str(cat2)], values=[str(filter)],
                                   aggfunc=aggFunctions[aggr], fill_value="" )

    table.round(2)
    xLabel, yLabel, value = convertCSVFormat(table.to_csv())
    height = len(yLabel)*35
    return render_template("pivot.html", x =xLabel,y=yLabel,v=value, yLength = height, row = str(cat1),
                           col=str(cat2),aggr= aggLabels[aggr], filter =filterLabels[filter] )


def convertCSVFormat(file):
    lines = file.split('\n')
    aggr = True
    value = True
    yLabels = []
    xLabels = []
    values = []
    x = 0
    for line in lines:
        items = line.split(',')
        if aggr:
            aggr = False
        else:
            if value:
                value = False
                for item in items[1:]:
                    yLabels.append(item)
            else:
                xLabels.append(items[0])
                y = 0
                for item in items[1:]:
                    try:
                        item = float(item)
                        values.append([x, y, round(item,2)])
                    except ValueError:
                        values.append([x, y, 0])
                    y += 1
                x += 1


    return(xLabels, yLabels, values)


if __name__ == "__main__":
    app.run()

