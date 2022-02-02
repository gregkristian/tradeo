// Line charting tool
// y: values
// x: dates

document.addEventListener("DOMContentLoaded", function () {
    var y_values = JSON.parse(document.getElementById('y_values').dataset.y_values); //
    var x_dates = JSON.parse(document.getElementById('x_dates').dataset.x_values); //

    // set the dimensions and margins of the graph
    var margin = { top: 20, right: 20, bottom: 50, left: 70 },
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // parse the date / time
    var parseTime = d3.timeParse("%a, %d %b %Y %H:%M:%S GMT");

    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    // define the line
    var valueline = d3.line()
        .x(function (d) { return x(d.date); })
        .y(function (d) { return y(d.close); });

    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    var svg = d3.select("#stock_chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // create the data
    var data = y_values.map(function (d, index) {
        return {
            date: parseTime(x_dates[index]),
            close: d
        };
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function (d) { return (d.date); }));
    y.domain([
        d3.min(data, function (d) { return d.close; }),
        d3.max(data, function (d) { return d.close; })]);

    // Add the valueline path.
    svg.append("path")
        .data([data])
        .attr("class", "line")
        .attr("d", valueline)
        .attr("stroke-width", 2)
        .attr("stroke", "#0078b0")
        .attr("fill","none");

    // Add the x Axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add the y Axis
    svg.append("g")
        .call(d3.axisLeft(y));

});
