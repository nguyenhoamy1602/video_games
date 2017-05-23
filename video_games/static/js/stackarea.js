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
                text: 'Unit Sales (million)'
            }
        },
        tooltip: {
            split: true,
            valueSuffix: ' millions'
        },
            plotOptions: {
        area: {
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
     series: series2
 });
});