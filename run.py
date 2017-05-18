from video_games import app
app.run(debug=True)

@app.route("/")
def hello():
    return "Hello World!"
