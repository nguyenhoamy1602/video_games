$(function() {
    $(regress_chart).highcharts({
        chart: {
          type: 'scatter',
          zoomType: 'xy'
        },
        title: {
          text: 'Global Games Sales (in million) vs Number of Games Released by Year'
        },
        subtitle: {
          text: 'Source: vgsales'
        },
        xAxis: {
          title: {
            text: 'Number of Games Released'
          }
        },       
        yAxis: {
          title: {
            text: 'Global Sales (million)'
          }
        },
        legend: {
          enabled: false,
        },
        
        tooltip: {
          formatter: function() {
            return ''+
            this.point.series.userOptions.data[this.point.index][2] + ' ' + this.x + ' games ' + this.y +' million sales';
          },
        },

        series: [{
            type: 'line',
            name: 'Regression Line',
            data: regress_series['Year'][0],
            marker: {
                enabled: false
            },
            states: {
                hover: {
                    lineWidth: 0
                }
            },
            enableMouseTracking: false
        }, {
            type: 'scatter',
            name: 'Observations',
            data: regress_series['Year'][1],
            marker: {
                radius: 4
            }
        }]
    });
});

$("#category-select").change(function () {
    var data_option = $(this).val();
    var chart = $(regress_chart).highcharts();  

    //change chart data
    chart.series[0].setData(regress_series[data_option][0],false);
    chart.series[1].setData(regress_series[data_option][1],false);
    chart.setTitle({text:"Global Games Sales (in million) vs Number of Games Released by " + data_option});

    $(regress_chart).highcharts().redraw();
}); 
