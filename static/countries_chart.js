function countriesFunc(vars){

//console.log(countires_vars['countries'])
//console.log(countires_vars['customers'])
                Chart.defaults.global.defaultFontFamily = 'Lato';
                Chart.defaults.global.defaultFontSize = 18;
                Chart.defaults.global.defaultFontColor = '#000';

                let my_countries_chart = document.getElementById("countries_chart").getContext("2d");

                let countries_chart = new Chart(my_countries_chart,{
                            type:'bar',
                            data:{
                                    labels: vars['countries'],
                                    datasets:[{ 
                                        data: vars['customers'],
                                        backgroundColor: [ "#F7464A", "#FDB45C", "#46BFBD"],
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
                                        text: 'Customer Base',
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
                                                labelString: 'No. of customers'
                                            }
                                        }],
                                        xAxes:[{
                                            scaleLabel:{
                                                display:true,
                                                labelString: 'Country'
                                            }
                                        }]
                                    }
                            }
                });

}