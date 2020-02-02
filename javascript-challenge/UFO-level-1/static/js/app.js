// from data.js
//var tableData = data;

// YOUR CODE HERE!
function renderTable(filteredData){
    var tbody = d3.select("tbody");

    filteredData.forEach((incident) => {
        var row = tbody.append("tr");
        Object.entries(incident).forEach(([key, value]) => {
            if(key != "comments") {
                var cell = row.append("td");
                cell.text(value);
            } else {
                var subrow = tbody.append("tr");
                subrow.append("td");
                subrow.append("td")
                    .attr("colspan", 5)
                    .text(value);
            };
        });
    });
}

var button = d3.select("#filter-btn");
button.on("click", function() {
    var rows = d3.selectAll("tr").remove();
    var parser = d3.timeParse("%Y-%m-%d")
    var formater = d3.timeFormat("%x")
    
    var dateElem = d3.select("#dateform");
    var dateVal = formater(parser(dateElem.property("value")));
    var filteredData = data.filter(d => d.datetime === dateVal);
    renderTable(filteredData);
});

renderTable(data);
