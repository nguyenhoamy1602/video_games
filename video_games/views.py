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
import json

from video_games import app, convert, chart

df = pd.read_csv('Data/vgsales.csv')

aggFunctions = {'count':np.count_nonzero, 'sum':np.sum, 'avg':np.mean,
            'min':np.min, 'max':np.max, 'med':np.median}
valueLabels = {'NA_Sales':'North America Sales', 'EU_Sales': 'Europe Sales', 'JP_Sales': 'Japan Sales',
                   'Other_Sales': 'Other Sales', 'Global_Sales':'Global Sales'}
aggLabels = {'count': 'Counting', 'sum': 'Sum ', 'avg': 'Average ',
             'min': 'Minimum ', 'max': 'Maximum ', 'med': 'Median '}

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/data")
def data():
    videogames = database.execute_query("""SELECT * FROM videogame""")
    return render_template("data.html", videogames=videogames)

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/pivot', methods=['GET', 'POST'])
def pivot():
    if request.method == 'POST':
        cat1 = request.form['cat1']
        cat2 = request.form['cat2']
        aggr = request.form['aggr']
        value = request.form['value']
        filter = request.form['filter']
        option = request.form['options']

        #pivots based on no filters
        if filter == 'none':
            table = pd.pivot_table(df, index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")
        #pivots based on year, it's different from next one bc Year was only filter with ints
        elif filter == 'Year':
            table = pd.pivot_table(df[df[filter] == int(option)], index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")
        #pivots based on any other filter
        else:
            table = pd.pivot_table(df[df[filter] == (option)], index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")

    #converts the pivot table into format that highcharts can understand
    xLabel, yLabel, values = convert.convertCSVFormat(table.to_csv(), cat1, cat2)
    # if y length or x length is size one then use predefined sizes, otherwise each cell should be at least 40x60px
    if len(yLabel)==1:
        height = 250
        width = len(xLabel)*60
    elif len(xLabel)==1:
        height = len(yLabel)*40
        width = 100
    else:
        height = len(yLabel)*40
        width = len(xLabel)*60
    # The title is different for count bc it's not counting in millions
    if aggr == "count":
        title = "Number of Video games sold in " +valueLabels[str(value)] +  "based on " + str(cat1) \
                + " and " + str(cat2)
    else:
        title = aggLabels[aggr] + " (in millions) in Sales for " + str(cat1) + " and " \
                + str(cat2)  + " in " + valueLabels[str(value)]
    return render_template("pivot.html", x =xLabel,y=yLabel,v=values, yLength = height, xLength = width, row = str(cat1),
                           col=str(cat2),aggr= aggLabels[aggr], filter =valueLabels[value], title = title )

@app.route('/bubblechart')
def bubble_chart():
    series = chart.chart4(df.dropna()[:1001])
    return render_template("bubble.html", series = series)


@app.route('/visualisation')
def visual():
    chartID_1 = 'chartID_1'
    x1,y1 = chart.chart1(df)
    chartID_2 = 'chartID_2'
    year,series2 = chart.chart2(df)
    chartID_3 = 'chart_ID_3'
    x3,series3 = chart.chart3(df)

    return render_template('visualisation.html', chartID_1=chartID_1, x1=x1,y1=y1,
        chartID_2=chartID_2, year=year, series2=series2, 
        x3=x3, series3=series3, chartID_3=chartID_3)



if __name__ == "__main__":
    app.run()

