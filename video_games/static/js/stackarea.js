$(document).ready(function() {
    $(chart_2).highcharts({
        chart: {
            type: 'area',
            zoomType:'xy'
        },
        title: {
            text: 'Sales Volume by Year'
        },
        subtitle: {
            text: 'Source: vgsales'
        },
        xAxis: {
            categories: year,
            tickmarkPlacement: 'on',
            title: {
                enabled: false
            }
        },
        yAxis: {
            title: {
                text: 'Sales Units'
            }
        },
        tooltip: {
            split: true,
            valueSuffix: ' millions'
        },
        plotOptions: {
            area: {
               stacking: 'normal',
               marker: {
                  radius: 2
              },
              lineWidth: 1,
              states: {
                  hover: {
                     lineWidth: 1
                 }
             },
             threshold: 0
         }
     },
     series: series2
 });
});