function clvFunc(vars) {
            am4core.ready(function() {                        
                        am4core.useTheme(am4themes_animated);
                        var chart = am4core.create("clv_chart", am4charts.PieChart3D);
                        chart.hiddenState.properties.opacity = 0;


                        chart.legend = new am4charts.Legend();

                        chart.data = [
                                {
                                    clv: "High CLV",
                                    values: vars['High Clv']
                                },
                                {
                                    clv: "Moderate CLV",
                                    values: vars['Mid Clv']
                                },
                                {
                                    clv: "Low CLV",
                                    values: vars['Low Clv']
                                }
                        ];

                        var series = chart.series.push(new am4charts.PieSeries3D());


                        var title = chart.titles.create();
                        title.text = "Customer Lifetime Value";
                        title.fontSize = 25;

                        series.dataFields.value = "values";
                        series.dataFields.category = "clv";

            });
}

/*
var colorSet = new am4core.ColorSet();
colorSet.list = ["#388E3C", "#A55336", "#0288d1"].map(function(color) {
return new am4core.color(color);
});
series.colors = colorSet;*/
            











/*





Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#000';

let my_piechart = document.getElementById("piechart").getContext("2d");

let piechart = new Chart(my_piechart,{
            type:'pie',
            data:{
                    labels: [ 'High CLV', 'Moderate CLV', 'Low CLV' ],
                    datasets:[{ 
                        label:'CLV',
                        data: [47,68,1100],
                        backgroundColor: [ "#FF6961", "#77DD77", "#6CA0DC"],
                        borderWidth:2,
                        borderColor: '#777',
                        hoverBorderWidth:3,
                        hoverBorderColor:'#000'
                        }]
                },
            options: {
                    responsive: false,
                    title:{
                        display:true,
                        text: 'Customer Lifetime Value',
                        fontSize:25
                    },
                    legend:{
                        display:true,
                        position:'right',
                        lables:{
                        fontColor:'#000'
                        }
                    },
                    layout:{
                        padding:{
                        left:50,
                        right:0,
                        bottom:0,
                        top:0
                        }
                    }
            }
});


*/