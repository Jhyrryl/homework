// from data.js
var tableData = data;

// YOUR CODE HERE!
function addOptions(options, elem) {
    options.forEach((option) => {
        elem.append("option")
            .attr("value", option)
            .text(option);
    });
}

var cities = []
var states = []
var countries = []
var shapes = []

tableData.forEach((incident) => {
    Object.entries(incident).forEach(([key, value]) => {
        if(key == "city") {
            if(!cities.includes(value)){
                cities.push(value)
            }
        }
        if(key == "state") {
            if(!states.includes(value)){
                states.push(value)
            }
        }
        if(key == "country") {
            if(!countries.includes(value)){
                countries.push(value)
            }
        }
        if(key == "shape") {
            if(!shapes.includes(value)){
                shapes.push(value)
            }
        }
    });
});

addOptions(cities.sort(), d3.select("#city_select"))
addOptions(states.sort(), d3.select("#state_select"))
addOptions(countries.sort(), d3.select("#country_select"))
addOptions(shapes.sort(), d3.select("#shape_select"))

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

    var cityElem = d3.select("#city_select");
    var cityVal = cityElem.property("value")
    
    var stateElem = d3.select("#state_select");
    var stateVal = stateElem.property("value")
    
    var countryElem = d3.select("#country_select");
    var countryVal = countryElem.property("value")
    
    var shapeElem = d3.select("#shape_select");
    var shapeVal = shapeElem.property("value")
    
    var filteredData = tableData.filter(d => {
        if(dateVal != "12/31/1969"){
            if(d.datetime != dateVal){
                return false;
            };
        }
        if((cityVal != "") && (d.city != cityVal)) {
            return false;
        };
        if((stateVal != "") && (d.state != stateVal)) {
            return false;
        };
        if((countryVal != "") && (d.country != countryVal)) {
            return false;
        };
        if((shapeVal != "") && (d.shape != shapeVal)) {
            return false;
        };
        return true;
    });
    renderTable(filteredData);
});

renderTable(tableData);
