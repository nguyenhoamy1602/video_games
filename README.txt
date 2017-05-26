# Video Games Sales Project
# By Melody, My and Alex

Application Content:
- The Data folder contains the data we use in our project
- The video-games folder contains our application 
	+ Python files to process datas
	+ The static folder contains all our css, js and img files
	+ The templates folder contains our html files


To run:
- Ensure you have installed Python and the required packages: flask, pandas and numpy
- Open command prompt, go to our project directory "cd video_games" 
- "python run.py" 
- Click on the localhost link produced

Note: Our application reference external resources from Bootstrap and Highcharts so you need a working Internet connection. You might also want to "Inspect" the page to see if the CSS is running normally. Chrome might block access to the resource page.


Our Application:
- Pivot Table - allow user to build their own pivot table
- Visualisation - our own intepretation of the data, trying to answering the questions of the best year, publisher, platform, genre and region for a game
- Bubble chart - an interactive chart for you to explore our top 1000 games according to genre

Note: All our charts allow for hovering to inspect individual points, zoom in by dragging your mouse drawing a rectangle and where legend is available, you can click on the legend to inspect individual series.


Tools:
- Pandas - To process data for pivot table and visualisations
- Highcharts - To draw interactive charts on website
- Flask - the structure for our application
- Jinja2 templates - providing templates for our HTML
- Bootstraps - Our CSS styling