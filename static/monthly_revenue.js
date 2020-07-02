function monthlyRevenueFunc(vars){

                Chart.defaults.global.defaultFontFamily = 'Lato';
                Chart.defaults.global.defaultFontSize = 18;
                Chart.defaults.global.defaultFontColor = '#000';

                let monthly_revenue = document.getElementById("monthly_revenue").getContext("2d");

                let monthly_revenue_chart = new Chart(monthly_revenue,{
                            type:'line',
                            data:{
                                    labels: vars['Date'],
                                    datasets:[{ 
                                        data: vars['Revenue'],
                                        fill: true,
                                        lineTension: 0.1,
                                        backgroundColor: "rgba(75,192,192,0.4)",
                                        borderColor: "rgba(75,192,192,1)",
                                        borderCapStyle: 'butt',
                                        borderDash: [],
                                        borderDashOffset: 0.0,
                                        borderJoinStyle: 'miter',
                                        pointBorderColor: "rgba(75,192,192,1)",
                                        pointBackgroundColor: "#fff",
                                        pointBorderWidth: 1,
                                        pointHoverRadius: 5,
                                        pointHoverBackgroundColor: "rgba(75,192,192,1)",
                                        pointHoverBorderColor: "rgba(220,220,220,1)",
                                        pointHoverBorderWidth: 2,
                                        pointRadius: 1,
                                        pointHitRadius: 10
                                        }]
                                },
                            options: {
                                    responsive: false,
                                    title:{
                                        display:true,
                                        text: 'Montly Revenue',
                                        fontSize:25
                                    },
                                    legend:{
                                        display:false,
                                        position:'right',
                                        lables:{
                                        fontColor:'#000'
                                        }
                                    },
                                    layout:{
                                        padding:{
                                        left:0,
                                        right:0,
                                        bottom:0,
                                        top:0
                                        }
                                    },
                                    scales:{
                                        yAxes:[{
                                            scaleLabel:{
                                                display:true,
                                                labelString: 'Revenue'
                                            }
                                        }],
                                        xAxes:[{
                                            scaleLabel:{
                                                display:true,
                                                labelString: 'Year - Month'
                                            }
                                        }]
                                    }
                            }
                });

}