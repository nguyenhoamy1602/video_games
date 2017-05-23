var text = "text";

$(document).ready(function() {
    $(chart_1).highcharts({
        chart: {
            zoomType: 'xy'
        },
        title: {
            text: 'Global Game Sales By Year'
        },
        subtitle: {
            text: 'Source: vgsales'
        },
        xAxis: [{
            categories: series1['Year'][0],
            crosshair: true
        }],
    yAxis: [{ // Primary yAxis
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        title: {
            text: 'Number of Games',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        }

    }, { // Secondary yAxis
        gridLineWidth: 0,
        title: {
            text: 'Sum of Global Sales (million)',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        },
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        },
        opposite: true,

    }, { // Tertiary yAxis
        max: 10,
        gridLineWidth: 0,
        title: {
            text: 'Unit Sales/Game (million)',
            style: {
                color: Highcharts.getOptions().colors[2]
            }
        },
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[2]
            }
        },
        opposite: true
    }],
    tooltip: {
        shared: true
    },
    series: [{
        name: 'Number of Games',
        type: 'column',
        yAxis: 0,
        data: series1['Year'][1],
        tooltip: {
            valueSuffix: ' games'
        }

    }, {
        name: 'Sum of Global Sales',
        type: 'line',
        yAxis: 1,
        data: series1['Year'][2],
        marker: {
            enabled: false
        },
        dashStyle: 'shortdot',
        tooltip: {
            valueSuffix: ' millon'
        }

    }, {
        name: 'Unit Sales/Game',
        type: 'line',
        yAxis: 2,
        data: series1['Year'][3],
        tooltip: {
            valueSuffix: ' million'
        }
    }]
});
});
var data_option = $('#travel-select').val();
    $("#travel-select").change(function () {
        var data_option = $(this).val();
        var chart = $(chart_1).highcharts();  
        var str = ""; 
        var i;
        //change chart data
        chart.xAxis[0].setCategories(series1[data_option][0]);
        for(i=0;i<3;i++){
            chart.series[i].setData(series1[data_option][i+1]);
        }
        if (data_option==="Year"){
            chart.setTitle({text:"Global Game Sales By Year"});
        } else {
            chart.setTitle({text:"Top Performing " + data_option});
        }
        $(chart_1).highcharts().redraw();
        $( "select option:selected" ).each(function() {
        str += text[data_option] + " ";
    });
    $( "#analysis" ).text( str );
    }); 

var text= {
    "Year": "The best year to release game is 2008 with highest Global Sales. " +
            "However, the year with the highest mean unit sales is 1989. " + 
            "Though total sales have decreased in recent year, " + 
            "mean unit sales per game has been relatively constant." 
    , "Genre": "The most prolific genre is Action. " + 
            "However, the genre with highest average sales is Platform."
    , "Publisher": "While Electronic Arts make the most game, " + 
                "Nintendo earns the most from the game market, " +
                "but Palcom has the highest average sales."
    , "Platform": "PS2 has the most games released and highest global sales. " +
                "GB has the highest average sales" 
}