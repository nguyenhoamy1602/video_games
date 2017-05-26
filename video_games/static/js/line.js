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
            crosshair: true,
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
$('.drop-down-show-hide').hide();
$('#Year').show();
var data_option = $('#travel-select').val();
    $("#travel-select").change(function () {
        var data_option = $(this).val();
        var chart = $(chart_1).highcharts();  
        var i;
        //change chart data
        chart.xAxis[0].setCategories(series1[data_option][0],false);
        for(i=0;i<3;i++){
            chart.series[i].setData(series1[data_option][i+1],false);
        }
        if (data_option==="Year"){
            chart.setTitle({text:"Global Game Sales By Year"});
        } else {
            chart.setTitle({text:"Top Performing " + data_option});
        }
        $(chart_1).highcharts().redraw();
        $( ".drop-down-show-hide").hide();
        $('#' + this.value).show();
    }); 

