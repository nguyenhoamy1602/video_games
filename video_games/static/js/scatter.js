$(document).ready(function() {
	$(chart_3).highcharts({
		chart: {
                type: 'scatter',
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
		series: series3['Year'][1]
    });
});

var data_option = $('#travel-select').val();
$("#travel-select").change(function () {
    var data_option = $(this).val();
    var chart3 = $(chart_3).highcharts(); 
    var i;
    //change chart data
    var category = series3[data_option][0];
    chart3.xAxis[0].setCategories(category);
    for(i=0;i<category.length;i++){
    chart3.series[i].setData(series3[data_option][1][i]);
    };
    chart3.setTitle({text:"Top 1000 Games Sales According to " + data_option});
    $(chart_3).highcharts().redraw();
    });