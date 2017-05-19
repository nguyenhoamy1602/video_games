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

from video_games import app, database, convert, chart

df = pd.read_csv('Data/vgsales.csv', nrows=1001)

aggFunctions = {'count':np.count_nonzero, 'sum':np.sum, 'avg':np.mean,
            'min':np.min, 'max':np.max, 'med':np.median}
valueLabels = {'NA_Sales':'North America Sales', 'EU_Sales': 'Europe Sales', 'JP_Sales': 'Japan Sales',
                   'Other_Sales': 'Other Sales', 'Global_Sales':'Global Sales'}
aggLabels = {'count': 'Counting', 'sum': 'Sum of', 'avg': 'Average of',
             'min': 'Minimum of', 'max': 'Maximum of', 'med': 'Median of'}

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
        if filter == 'none':
            table = pd.pivot_table(df, index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")
        elif filter == 'Year':
            table = pd.pivot_table(df[df[filter] == int(option)], index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")
        else:
            table = pd.pivot_table(df[df[filter] == (option)], index=[str(cat1)], columns=[str(cat2)],
                                   values=[str(value)],
                                   aggfunc=aggFunctions[aggr], fill_value="")


    xLabel, yLabel, values = convert.convertCSVFormat(table.to_csv(), cat1, cat2)
    height = len(yLabel)*40
    width = len(xLabel)*60
    return render_template("pivot.html", x =xLabel,y=yLabel,v=values, yLength = height, xLength = width, row = str(cat1),
                           col=str(cat2),aggr= aggLabels[aggr], filter =valueLabels[value] )

@app.route('/bubblechart')
def bubble_chart():
    Genres = database.execute_query("SELECT distinct Genre from videogame order by Genre asc")
    series = []
    for Genre in Genres:
        data = []
        videogames = database.execute_query("SELECT * from videogame where Genre = ? and Year IS NOT \"N/A\"", (Genre[0],))
        for videogame in videogames:
            data.append({ 'name': videogame['Name'], 'publisher': videogame['Publisher'], 'y': videogame['Global_Sales'], 'x': videogame['Year'], 'z': videogame['Global_Sales']})
        series.append({ 'name': Genre[0], 'data': data })
    return render_template("bubble.html", series = json.dumps(series))


@app.route('/visualisation')
def visual():
    plot_url = chart.chart1(df)

    return render_template('visualisation.html', plot_url=plot_url)


if __name__ == "__main__":
    app.run()

