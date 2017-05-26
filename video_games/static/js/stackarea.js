$(document).ready(function() {
    $(region_chart).highcharts({
        chart: {
            type: 'area',
            zoomType:'xy'
        },
        title: {
            text: 'Sales Volume by Year and Region'
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
     series: region_series
 });
});