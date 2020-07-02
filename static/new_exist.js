function newExistFunc(vars){                   
                    Chart.defaults.global.defaultFontFamily = 'Lato';
                    Chart.defaults.global.defaultFontSize = 18;
                    Chart.defaults.global.defaultFontColor = '#000';

                    let new_exist = document.getElementById("new_exist").getContext("2d");



                    var mixedChart = new Chart(new_exist, {
                        type: 'line',
                        data: {
                            datasets: [{
                                label: 'Existing Customers',
                                data: vars['Exist'],
                                fill:false,
                                borderColor:"rgba(255,0,2,1)"
                            }, {
                                label: 'New Customers',
                                data: vars['New'],
                                type: 'line',
                                fill: false,
                                borderColor:"rgba(0,1,192,1)"
                            }],
                            labels: vars['Date'],
                        },
                        options: {
                            responsive: false,
                            title:{
                                display:true,
                                text: 'New vs Existing Customers Revenue',
                                fontSize:25
                            },
                            legend:{
                                display:true,
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