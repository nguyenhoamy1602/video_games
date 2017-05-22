$(document).ready(function() {
    $(chart_1).highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Number of Game Released by Year'
        },
        subtitle: {
            text: 'Source: vgsales'
        },
        xAxis: {
            categories: x1
        },
        yAxis: {
            title: {
                text: 'Number of Game'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: false
                },
                enableMouseTracking: true
            }
        },
        series: [{
           name: 'Number of Game',
           data: y1
       }]
   });
});