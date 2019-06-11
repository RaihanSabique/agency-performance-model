
var mappedData = [];

d3.json('http://127.0.0.1:5000/agency/3', function(data) {
    console.log("hit")
    console.log(data);
    var dlist = d3.entries(data);
    console.log(dlist)
    var max_width=-9999

    for (var i = 0; i < data.length; i++) {
      var eachObjArr = [];
      for (key in data[i]) {
        if (data[i].hasOwnProperty(key)) {
          var obj = {};
          obj[key] = data[i][key];
          mappedData.push({ axis: key, value: data[i][key] });
        }
      }console.log()

    }

    for (var i = 0; i < mappedData.length; i++) {
      console.log(mappedData[i]);
      console.log(mappedData[i].value);
      if(mappedData[i].value>max_width)
            {max_width=mappedData[i].value}
    }

        var width=500;
        var height=500;

        var widthScale=d3.scaleLinear()
                       .domain([0,max_width])
                       .range([0,width])

        var color=d3.scaleLinear()
                  .domain([0,max_width])
                  .range(["red","blue"])



        var canvas=d3.select("body")
                    .append("svg")
                    .attr("width",width)
                    .attr("height",height)
                    .append("g")
                    .attr("transform","translate(20,0)")

        var bars=canvas.selectAll("rect")
                     .data(mappedData)
                     .enter()
                        .append("rect")
                        .attr("width", function(d){console.log(d.value); return widthScale(d.value);})
                        .attr("height", 40)
                        .attr("fill", function(d,i){return color(d.value);})
                        .attr("y", function(d,i) {return i*50})
});

var dataArr=[20,30,25]






