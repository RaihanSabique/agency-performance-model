
//window.onload=function() {
//var submit=document.getElementById("btn_get_agency_id");
//submit.onclick=function(){
 //   var id=document.getElementById("agency_id").value;
   // agency_id=id
id=d3.select("g.tooltip > text.name").text();;



d3.json('http://127.0.0.1:5000/agency/'+id, function(data) {
    var mappedData = [];
    var types=3
    for ( var i = 0; i < types; i++ ) {
        mappedData[i] = [];
    }
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
          mappedData[i].push({ name: key, value: data[i][key] });
        }
      }console.log()

    }

    for (var i = 0; i < mappedData[0].length; i++) {
      console.log(mappedData[0][i]);
      console.log(mappedData[0][i].value);
      if(mappedData[0][i].value>max_width)
            {max_width=mappedData[0][i].value}
    }
    var cl_percentage,pl_percentage
    for (var i = 0; i < mappedData[1].length; i++) {
      console.log(mappedData[1][i]);
      if(mappedData[1][i].name=="CL"){cl_percentage=mappedData[1][i].value}
      else {pl_percentage=mappedData[1][i].value}
     }
     console.log(pl_percentage,cl_percentage)

     var cl_list=[]
         pl_list=[]
     for (var i = 0; i < mappedData[2].length; i++) {
      console.log(mappedData[2][i]);
      if(i==0){
        cl_list=mappedData[2][i].value
      }
      if(i==1){
        pl_list=mappedData[2][i].value
      }

     }
     console.log(cl_list);


var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 900 - margin.left - margin.right,
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


var svg_state_bar = d3.select("#state_bar").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "bar-svg-component")
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  // format the data
  mappedData[0].forEach(function(d) {
    d.value = +d.value;
  });

  // Scale the range of the data in the domains
  x.domain([0, d3.max(mappedData[0], function(d){ return d.value; })])
  y.domain(mappedData[0].map(function(d) { return d.name; }));
  //y.domain([0, d3.max(data, function(d) { return d.sales; })]);

  // append the rectangles for the bar chart
  svg_state_bar.selectAll(".bar")
      .data(mappedData[0])
    .enter().append("rect")
      .attr("class", "bar")
      //.attr("x", function(d) { return x(d.sales); })
      .attr("width", function(d) {return x(d.value); } )
      .attr("y", function(d) { return y(d.name); })
      .attr("fill", function(d){return color(d.value);})
      .attr("height", y.bandwidth());

  // add the x Axis
  svg_state_bar.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // add the y Axis
  svg_state_bar.append("g")
      .call(d3.axisLeft(y));

//percentage bar of product line


let chart = radialProgress('#cl_radial',"progress-bar-1")
let progress = [0,cl_percentage]
let state = 1
let chart2 = radialProgress('#pl_radial',"progress-bar-2")
let progress2 = [0,pl_percentage]
let state2 = 0
d3.interval(function(){
  chart.update(progress[state])
  state = (state + 1) % progress.length
  chart2.update(progress2[state2])
  state2 = (state2 + 1) % progress2.length
}, 1500)

var cl_names = d3.select('#cl_name').append('ul');

	cl_names.selectAll('li')
	.data(cl_list)
	.enter()
	.append('li')
	.attr('class','cl_text')
	.append('strong')
	.html(String);

var pl_names = d3.select('#pl_name').append('ul');

	pl_names.selectAll('li')
	.data(pl_list)
	.enter()
	.append('li')
	.attr('class','pl_text')
	.append('strong')
	.html(String);


});


//}


//}


function radialProgress(selector,bar_color) {
    var parent = d3.select(selector)
    var size = parent.node().getBoundingClientRect()
    var svg = parent.append('svg')
    .attr('width', size.width)
    .attr('height', size.height);
  var outerRadius = Math.min(size.width, size.height) * 0.45;
  var thickness = 10;
  let value = 0;

  var mainArc = d3.arc()
    .startAngle(0)
    .endAngle(Math.PI * 2)
    .innerRadius(outerRadius-thickness)
    .outerRadius(outerRadius)

  svg.append("path")
    .attr('class', 'progress-bar-bg')
    .attr('transform', `translate(${size.width/2},${size.height/2})`)
    .attr('d', mainArc())

  var mainArcPath = svg.append("path")
    .attr('class', bar_color)
    .attr('transform', `translate(${size.width/2},${size.height/2})`)

  svg.append("circle")
    .attr('class', bar_color)
    .attr('transform', `translate(${size.width/2},${size.height/2-outerRadius+thickness/2})`)
    .attr('width', thickness)
    .attr('height', thickness)
    .attr('r', thickness/2)

  var end = svg.append("circle")
    .attr('class', bar_color)
    .attr('transform', `translate(${size.width/2},${size.height/2-outerRadius+thickness/2})`)
    .attr('width', thickness)
    .attr('height', thickness)
    .attr('r', thickness/2)

  let percentLabel = svg.append("text")
    .attr('class', 'progress-label')
    .attr('transform', `translate(${size.width/2},${size.height/2})`)
    .text('0%')

  return {
    update: function(progressPercent) {
      var startValue = value
      var startAngle = Math.PI * startValue / 50
      var angleDiff = Math.PI * progressPercent / 50 - startAngle;
      var startAngleDeg = startAngle / Math.PI * 180
      var angleDiffDeg = angleDiff / Math.PI * 180
      var transitionDuration = 1500

      mainArcPath.transition().duration(transitionDuration).attrTween('d', function(){
        return function(t) {
          mainArc.endAngle(startAngle + angleDiff * t)
          return mainArc();
        }
      })

      end.transition().duration(transitionDuration).attrTween('transform', function(){
        return function(t) {
          return `translate(${size.width/2},${size.height/2})`+
            `rotate(${(startAngleDeg + angleDiffDeg * t)})`+
            `translate(0,-${outerRadius-thickness/2})`
        }
      })

      percentLabel.transition().duration(transitionDuration).tween('bla', function() {
        return function(t) {
          percentLabel.text(Math.round(startValue + (progressPercent - startValue) * t)+'%');
        }
      })
      value = progressPercent
    }
  }
}

