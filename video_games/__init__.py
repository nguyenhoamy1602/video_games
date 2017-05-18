import sys, os

# Add /vendor and /lib to python PATH
sys.path.append(os.path.join(os.path.dirname(__file__), "../vendor"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from flask import Flask, g
app = Flask(__name__)
app.config.from_object('config')

from video_games import views
import video_games.database
