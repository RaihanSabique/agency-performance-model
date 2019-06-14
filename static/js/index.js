
//window.onload=function() {
//var submit=document.getElementById("btn_get_agency_id");
//submit.onclick=function(){
 //   var id=document.getElementById("agency_id").value;
   // agency_id=id
id=d3.select("g.tooltip > text.name").text();;

var mappedData = [];

d3.json('http://127.0.0.1:5000/agency/'+id, function(data) {
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
          mappedData.push({ name: key, value: data[i][key] });
        }
      }console.log()

    }

    for (var i = 0; i < mappedData.length; i++) {
      console.log(mappedData[i]);
      console.log(mappedData[i].value);
      if(mappedData[i].value>max_width)
            {max_width=mappedData[i].value}
    }

        /*var margin = {
            top: 15,
            right: 25,
            bottom: 15,
            left: 60
        };

        var width=500 -margin.left -margin.right;
        var height=500 - margin.top-margin.bottom;

        var widthScale=d3.scaleLinear()
                       .domain([0,max_width+20])
                       .range([0,width])

        var x = d3.scaleLinear()
            .range([0, width])
            .domain([0, d3.max(mappedData, function (d) {
                return d.value;
            })]);

        var y = d3.scaleOrdinal()
            .range([0,300])
            .domain(mappedData.map(function (d) {
                return d.axis;
            }));

        var color=d3.scaleLinear()
                  .domain([0,max_width])
                  .range(["red","blue"])
        var xAxis = d3.axisBottom(widthScale)


        var canvas=d3.select("#graphic")
                    .append("svg")
                    .attr("width",width+margin.left+margin.right)
                    .attr("height",height+margin.top+margin.bottom)
                    .append("g")
                    .attr("transform","translate(" + margin.left + "," + margin.top + ")")

        var bars=canvas.selectAll("rect")
                     .data(mappedData)
                     .enter()
                        .append("rect")
                        //.append("text")
                        .attr("width", function(d){console.log(d.value); return x(d.value);})
                        .attr("height", 40)
                        .attr("fill", function(d,i){return color(d.value);})
                        .attr("y", function(d,i) {return i*50})
                        //.text(function(d){return y(d.axis)})
        canvas.append("g")
                .attr("transform","translate(0,300)")
                .call(xAxis)

        bars.append("text")
            .data(mappedData)
            .enter()
                .attr("class", "label")
                //y position of the label is halfway down the bar
                .attr("y", function(d,i) {return i*50})
                //x position is 3 pixels to the right of the bar
                .attr("x", function (d) {
                    return x(d.value) + 3;
                })
                .text(function (d) {
                    return x(d.value);
                });*/

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 800 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// set the ranges
var y = d3.scaleBand()
          .range([height, 0])
          .padding(0.1);

var x = d3.scaleLinear()
          .range([0, width]);

var color=d3.scaleLinear()
            .domain([0,max_width])
            .range(["red","blue"])

// append the svg object to the body of the page
// append a 'group' element to 'svg'
// moves the 'group' element to the top left margin
d3.select("#state_text")
            .append("h4")
            .append("strong")
            .attr("style","color:#51768C")
            .text("Bar chart represented total operational number of individual six state with agency "+id)


var svg = d3.select("#state_bar").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "bar-svg-component")
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  // format the data
  mappedData.forEach(function(d) {
    d.value = +d.value;
  });

  // Scale the range of the data in the domains
  x.domain([0, d3.max(mappedData, function(d){ return d.value; })])
  y.domain(mappedData.map(function(d) { return d.name; }));
  //y.domain([0, d3.max(data, function(d) { return d.sales; })]);

  // append the rectangles for the bar chart
  svg.selectAll(".bar")
      .data(mappedData)
    .enter().append("rect")
      .attr("class", "bar")
      //.attr("x", function(d) { return x(d.sales); })
      .attr("width", function(d) {return x(d.value); } )
      .attr("y", function(d) { return y(d.name); })
      .attr("fill", function(d){return color(d.value);})
      .attr("height", y.bandwidth());

  // add the x Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // add the y Axis
  svg.append("g")
      .call(d3.axisLeft(y));




});

var dataArr=[20,30,25]

//}


//}




