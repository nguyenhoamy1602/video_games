$(document).ready(function() {
    $(bubble).highcharts({

    chart: {
        type: 'bubble',
        plotBorderWidth: 1,
        zoomType: 'xy'
    },

    legend: {
        enabled: true,
    },

    title: {
        text: "Top 1000 Video Game's Sales and Year Released"
    },

    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: "Sales in million",
            style: {
                fontSize: '20px'
            }, 
        }
    },

    tooltip: {
        useHTML: true,
        headerFormat: '<table>',
        pointFormat: '<tr><th colspan="2"><h3>{point.name}</h3></th></tr>' +
            '<tr><th>Publisher:</th><td>{point.publisher}</td></tr>' +
            '<tr><th>Genre: </th><td>{point.genre}</td></tr>' +
            '<tr><th>Year:</th><td>{point.x}</td></tr>' +
            '<tr><th>Sale(million):</th><td>{point.y}</td></tr>',
        footerFormat: '</table>',
        followPointer: true
    },

    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '{point.name}',
                color: 'black'
            }
        }
    },

    series: series

    });
});