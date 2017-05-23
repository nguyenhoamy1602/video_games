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
        categories: year1,
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
    legend: {
        layout: 'vertical',
        align: 'left',
        x: 80,
        verticalAlign: 'top',
        y: 55,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
    },
    series: [{
        name: 'Number of Games',
        type: 'column',
        yAxis: 0,
        data: series1[0],
        tooltip: {
            valueSuffix: ' games'
        }

    }, {
        name: 'Sum of Global Sales',
        type: 'line',
        yAxis: 1,
        data: series1[1],
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
        data: series1[2],
        tooltip: {
            valueSuffix: ' million'
        }
    }]
});
});