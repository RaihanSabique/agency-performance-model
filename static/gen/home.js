var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 80},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var tooltip = d3.select("body").append("div").attr("class", "toolTip");

var x = d3.scaleLinear().range([0, width]);
var y = d3.scaleBand().range([height, 0]);

var g = svg.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.json('http://127.0.0.1:5000/agency/3', function(data) {
    console.log("hit")
    console.log(data);
    var dlist = d3.entries(data);
    console.log(dlist)

    mappedData = [];

    for (var i = 0; i < data.length; i++) {
      var eachObjArr = [];
      for (key in data[i]) {
        if (data[i].hasOwnProperty(key)) {
          var obj = {};
          obj[key] = data[i][key];
          eachObjArr.push({ axis: key, value: data[i][key] });
        }
      }console.log()
      mappedData.push(eachObjArr);
    }

    for (var i = 0; i < mappedData.length; i++) {
      console.log(mappedData[i]);
    }
});
