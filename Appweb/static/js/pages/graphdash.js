/* radar chart */
var optionsRadar = {
    series: [{
    data: [60,70,40,20]
  }],
    chart: {
    height: 500,
    type: 'radar',
  },



  xaxis: {
    categories: ["Scientist","Engineer","Analyst","Manager"]
    
 }
  };
  
  var chartRadar = new ApexCharts(document.querySelector("#chartRadar"), optionsRadar);
  chartRadar.render();
  


  // Distribution Competence

  var options = {
    series: [{
    data: [21, 22, 10, 28, 16, 21, 13]
  }],


    chart: {
    height: 350,
    type: 'bar',
    events: {
      click: function(chart, w, e) {
        // console.log(chart, w, e)
      }
    }
  },
  
  plotOptions: {
    bar: {
      columnWidth: '45%',
      distributed: true,
    }
  },
  dataLabels: {
    enabled: false
  },
  legend: {
    show: true
  },
  xaxis: {
    categories: [
      ['Python'],
      ['Sql'],
      ['Javascript'],     
      ['R'],
      ['C++'],
      ['C'],
      ['Vs-Code'], 
    ],
    labels: {
      style: {
        
        fontSize: '12px'
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

