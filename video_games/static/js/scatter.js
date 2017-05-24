var options = {
    chart: {
        renderTo: chart_3,
        defaultSeriesType: 'scatter',
        zoomType: 'xy',
            },
            title: {
                text: 'Top 1000 Games Sales According to Year'
            },
            subtitle: {
                text: 'Source: vgsales'
            },
        xAxis: {
                categories: series3['Year'][0]
            },
        yAxis: {"title": {"text": 'Unit Sales (million)'}},
        tooltip: {
                formatter: function() {
                        return ''+
                        this.point.series.userOptions.data[this.point.index][2] + ' ' + this.y +' million';
                }
            },
        legend: {
            enabled: false
        },
        plotOptions: {
                scatter: {
                    marker: {
                        symbol:'circle',
                        radius: 5,
                        states: {
                            hover: {
                                enabled: true,
                                lineColor: 'rgb(100,100,100)'
                            }
                        }
                    },
                    states: {
                        hover: {
                            marker: {
                                enabled: false
                            }
                        }
                    }
                }
        },
    series: series3['Year'][1],
};
var chart = new Highcharts.Chart(options);

$('#travel-select').on('change', function(){
    //alert('f')
    var data_option = $('#travel-select').val();
    options.series = series3[data_option][1];
    options.title.text = 'Top 1000 Games Sales According to' + data_option;
    options.xAxis.categories = series3[data_option][0];
    var chart = new Highcharts.Chart(options);    
});

