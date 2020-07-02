function monthlyActiveFunc(vars){

            Chart.defaults.global.defaultFontFamily = 'Lato';
            Chart.defaults.global.defaultFontSize = 18;
            Chart.defaults.global.defaultFontColor = '#000';

            let monthly_active = document.getElementById("monthly_active").getContext("2d");

            let monthly_active_chart = new Chart(monthly_active,{
                        type:'bar',
                        data:{
                                labels: vars['Date'],
                                datasets:[{ 
                                    data: vars['Active'],
                                    backgroundColor:"#4169E199",
                                    fill: true,
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
                                    text: 'Montly Active Customers',
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
                                            labelString: 'No. of Customers'
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
