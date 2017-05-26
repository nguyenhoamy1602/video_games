$(function() {
  $(chart_4).highcharts({
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
        data: series4['Year'][0],
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
        data: series4['Year'][1],
        marker: {
            radius: 4
        }
    }]
});
});
    $("#travel-select").change(function () {
        var data_option = $(this).val();
        var chart4 = $(chart_4).highcharts();  

        //change chart data
        chart4.series[0].setData(series4[data_option][0],false);
        chart4.series[1].setData(series4[data_option][1],false);
        chart4.setTitle({text:"Global Games Sales (in million) vs Number of Games Released by " + data_option});

        $(chart_4).highcharts().redraw();
    }); 
