$(document).ready(function() {
	$(chart_3).highcharts({
		chart: {
                type: 'scatter',
                zoomType: 'xy',
            },
            title: {
                text: 'Sales Units according to Genre'
            },
            subtitle: {
                text: 'Source: vgsales'
            },
		xAxis: {
                title: {
                    enabled: true,
                    text: 'Genre'
                },
                categories: x3
            },
		yAxis: {"title": {"text": 'Sale Units in million'}},
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
		series: series3
	});
});