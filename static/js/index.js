
//window.onload=function() {
//var submit=document.getElementById("btn_get_agency_id");
//submit.onclick=function(){
 //   var id=document.getElementById("agency_id").value;
   // agency_id=id
id=d3.select("g.tooltip > text.name").text();;



d3.json('http://ec2-18-217-184-154.us-east-2.compute.amazonaws.com/agency/'+id, function(data) {
    var mappedData = [];
    var nb_wrtn_prem_amt=[]
        total_wrtn_prem_amt=[]
        prev_wrtn_prem_amt=[]
        ernd_prem_amt=[]
        losses_amt=[]
        min_value=9999
        max_value=-9999

    var types=4
    for ( var i = 0; i < types; i++ ) {
        mappedData[i] = [];
    }
    console.log("hit")
    console.log(data);
    var dlist = d3.entries(data);
    console.log(dlist)
    var max_width=-9999
    var chart_data=[]
    let parseDate = d3.timeParse("%Y");

    for (var i = 0; i < types; i++) {
      var eachObjArr = [];
      if(i==3){
        console.log(data[i])
        for(key in data[i]){
            if(key=='nb_wrtn_prem_amt'){
                var obj={};
                obj[key]=data[i][key]
                for(k in obj[key]){
                    nb_wrtn_prem_amt.push({year:k,value:obj[key][k]})
                    if(obj[key][k]>max_value){max_value=obj[key][k]}
                    if(obj[key][k]<min_value){min_value=obj[key][k]}
                }
            }
            if(key=='total_wrtn_prem_amt'){
                var obj={};
                obj[key]=data[i][key]
                for(k in obj[key]){
                    total_wrtn_prem_amt.push({year:k,value:obj[key][k]})
                    if(obj[key][k]>max_value){max_value=obj[key][k]}
                    if(obj[key][k]<min_value){min_value=obj[key][k]}
                }
            }
            if(key=='prev_wrtn_prem_amt'){
                var obj={};
                obj[key]=data[i][key]
                for(k in obj[key]){
                    prev_wrtn_prem_amt.push({year:k,value:obj[key][k]})
                    if(obj[key][k]>max_value){max_value=obj[key][k]}
                    if(obj[key][k]<min_value){min_value=obj[key][k]}
                }
            }
            if(key=='ernd_prem_amt'){
                var obj={};
                obj[key]=data[i][key]
                for(k in obj[key]){
                    ernd_prem_amt.push({year:k,value:obj[key][k]})
                    if(obj[key][k]>max_value){max_value=obj[key][k]}
                    if(obj[key][k]<min_value){min_value=obj[key][k]}
                }
            }
            if(key=='losses_amt'){
                var obj={};
                obj[key]=data[i][key]
                for(k in obj[key]){
                    losses_amt.push({year:k,value:obj[key][k]})
                    if(obj[key][k]>max_value){max_value=obj[key][k]}
                    if(obj[key][k]<min_value){min_value=obj[key][k]}
                }
            }
        }
      }
      else{
        for (key in data[i]) {
        if (data[i].hasOwnProperty(key)) {
          var obj = {};
          obj[key] = data[i][key];
          mappedData[i].push({ name: key, value: data[i][key] });
        }
      }console.log()

      }

    }

    console.log(losses_amt)
    console.log(min_value)
    console.log(max_value)


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
let progress = [cl_percentage]
let state = 0
let chart2 = radialProgress('#pl_radial',"progress-bar-2")
let progress2 = [pl_percentage]
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


//line graph
var vis = d3.select("#visualisation"),
                        WIDTH = 750,
                        HEIGHT = 500,
                        MARGINS = {
                            top: 20,
                            right: 20,
                            bottom: 20,
                            left: 100
                        },
                        xScale = d3.scaleLinear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([2005,2015]),
                        yScale = d3.scaleLinear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([min_value, max_value]),
                        xAxis = d3.axisBottom().scale(xScale),
                        yAxis = d3.axisLeft().scale(yScale);


                    vis.append("svg:g")
                        .attr("class", "x axis")
                        .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
                        .call(xAxis);
                    vis.append("svg:g")
                        .attr("class", "y axis")
                        .attr("transform", "translate(" + (MARGINS.left) + ",0)")
                        .call(yAxis);
                    vis.append("g")
                      .append("text")
                        .attr("class", "axis-title")
                        .attr("transform", "rotate(-90)")
                        .attr("y", 20)
                        .attr("dy", ".71em")
                        .style("text-anchor", "end")
                        .attr("fill", "#5D6971")
                        .text("USD");

                    var lineGen = d3.line()
                        .x(function(d) {
                            return xScale(d.year);
                        })
                        .y(function(d) {
                            return yScale(d.value);
                        })


                    vis.append('svg:path')
                        .attr('d', lineGen(nb_wrtn_prem_amt))
                        .attr('stroke', 'green')
                        .attr('stroke-width', 4)
                        .attr('fill', 'none');
                    vis.append('svg:path')
                        .attr('d', lineGen(total_wrtn_prem_amt))
                        .attr('stroke', '#F3B900')
                        .attr('stroke-width', 4)
                        .attr('fill', 'none');

                    vis.append('svg:path')
                        .attr('d', lineGen(prev_wrtn_prem_amt))
                        .attr('stroke', '#26BFBF')
                        .attr('stroke-width', 4)
                        .attr('fill', 'none');
                    vis.append('svg:path')
                        .attr('d', lineGen(ernd_prem_amt))
                        .attr('stroke', '#313A87')
                        .attr('stroke-width', 4)
                        .attr('fill', 'none');

                    vis.append('svg:path')
                        .attr('d', lineGen(losses_amt))
                        .attr('stroke', 'red')
                        .attr('stroke-width', 4)
                        .attr('fill', 'none');

/*var svg = d3.select("#graph"),
        margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom;

var parseTime = d3.timeParse("%Y")
    bisectDate = d3.bisector(function(d) { return d.year; }).left;

var x = d3.scaleTime().range([0,width]);
var y = d3.scaleLinear().range([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.value); });

var scale = d3.scaleLinear()
                  .domain([min_value,max_value])
                  .range([min_value,max_value]);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y).ticks(6).tickFormat(function(d) { return parseInt(d / 1000) + "k"; }))
      .append("text")
        .attr("class", "axis-title")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .attr("fill", "#5D6971")
        .text("USD)");

           draw_graph(nb_wrtn_prem_amt);
           draw_graph(total_wrtn_prem_amt);
           draw_graph(prev_wrtn_prem_amt);
           draw_graph(ernd_prem_amt);
           draw_graph(losses_amt);

function draw_graph (data) {

    data.forEach(function(d) {
      d.year = parseTime(d.year);
      d.value = +d.value;
    });

    x.domain(d3.extent(data, function(d) { return d.year; }));
    y.domain([d3.min(data, function(d) { return d.value; }) / 1.005, d3.max(data, function(d) { return d.value; }) * 1.005]);



    g.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", line);

    var focus = g.append("g")
        .attr("class", "focus")
        .style("display", "none");

    focus.append("line")
        .attr("class", "x-hover-line hover-line")
        .attr("y1", 0)
        .attr("y2", height);

    focus.append("line")
        .attr("class", "y-hover-line hover-line")
        .attr("x1", width)
        .attr("x2", width);

    focus.append("circle")
        .attr("r", 7.5);

    focus.append("text")
        .attr("x", 15)
      	.attr("dy", ".31em");

    svg.append("rect")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
        .attr("class", "overlay")
        .attr("width", width)
        .attr("height", height)
        .on("mouseover", function() { focus.style("display", null); })
        .on("mouseout", function() { focus.style("display", "none"); })
        .on("mousemove", mousemove);

    function mousemove() {
      var x0 = x.invert(d3.mouse(this)[0]),
          i = bisectDate(data, x0, 1),
          d0 = data[i - 1],
          d1 = data[i],
          d = x0 - d0.year > d1.year - x0 ? d1 : d0;
      focus.attr("transform", "translate(" + x(d.year) + "," + y(d.value) + ")");
      focus.select("text").text(function() { return d.value; });
      focus.select(".x-hover-line").attr("y2", height - y(d.value));
      focus.select(".y-hover-line").attr("x2", width + width);
    }
}*/



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




