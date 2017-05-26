var scatter_options = {
    chart: {
        renderTo: scatter_chart,
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
                categories: scatter_series['Year'][0],
                tickPositioner: function() {
                var result = [];
                for(i = 0; i < scatter_series['Year'][0].length; i++)
                    result.push(i);
                return result;
                }
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
    series: scatter_series['Year'][1],
};
var chart = new Highcharts.Chart(scatter_options);

$('#travel-select').on('change', function(){
    //alert('f')
    var data_option = $('#travel-select').val();
    scatter_options.series = scatter_series[data_option][1];
    scatter_options.title.text = 'Top 1000 Global Games Sales According to ' + data_option;
    scatter_options.xAxis.categories = scatter_series[data_option][0];
    var chart = new Highcharts.Chart(scatter_options);    
});

