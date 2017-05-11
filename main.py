# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:14:54 2017

@author: melod
"""

# Import all libraries needed for the tutorial
# Import all libraries needed for the tutorial
from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)
df = pd.read_csv("Data/vgsales.csv")

@app.route('/')
def index():
    return 'This is the homepage'

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
        if str(aggr) == 'All':
            table = pd.pivot_table(df, index=[str(cat1), str(cat2)], values=["NA_Sales","EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], aggfunc=[np.sum])
        else:
            table = pd.pivot_table(df,index=[str(cat1),str(cat2)], values=[str(aggr)],aggfunc=[np.sum] )
    return render_template("pivot.html", table=table.to_html())



# @app.route("/bacon" , methods=['GET', 'POST'])
# def bacon():
#     if request.method == 'POST':
#         return "You are using post"
#     else:
#         return "You are probably using GET"

if __name__ == "__main__":
    app.run()

