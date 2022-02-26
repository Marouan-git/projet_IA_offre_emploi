/* radar chart */
var optionsRadar = {
    series: [{
    data: nombre_annonce
  }],
    chart: {
    height: 500,
    type: 'radar',
  },

  legend: {
    show: true
    
  },

  dataLabels: {
    enabled: true,
    background: {
      enabled: true,
      borderRadius:2,
    }
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
    data: occurence
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
    enabled: true
  },
  legend: {
    show: false
  },
  xaxis: {
    categories: keyword
      
    ,
    labels: {
      style: {
        fontSize: '15px'
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

