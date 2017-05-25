import sys, os

from flask import Flask, g
app = Flask(__name__)
app.config.from_object('config')

from video_games import views
