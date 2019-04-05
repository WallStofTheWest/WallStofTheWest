
// var tableBodyName = "#main_tbody"

// function createtable (endpoint){
//     // cleartable()
//     console.log(`Display data for ${endpoint.replace("/", "")}`)
//     var tbody_main = d3.select(tableBodyName)
//     d3.json(endpoint, function(data) {
//         $('#table').bootstrapTable('load',data)
//         $('#table').bootstrapTable('selectPage',1)
//         // $('#table').bootstrapTable('load',data)
//         console.log($('#table').bootstrapTable('getVisibleColumns'))

//         });
//     }

// function cleartable (){
//     var tbody_main = d3.select(tableBodyName)
//     tbody_main.remove()

// }

// function init(){
//     $(".btn btn-secondary:first-child").text("EBITA");
//     $(".btn btn-secondary:first-child").val("EBITA");
//     createtable("/ebita_multiple")

// }
// method to change small table, it takes input of current table header value and top bottom button selection
function changesmalltable(current_table_value,top_bottom){
        let endpoint = "/top_bottom";
        // construct query using the end point and current table value and seperate by ',' which is then split in the endpoint
        let query_string = endpoint + current_table_value + ',' + top_bottom;
        console.log(query_string);
        document.getElementById("small_table").setAttribute("data-url", query_string);
        $('#small_table').bootstrapTable('refresh',{"url":query_string});
}

// function changetext(theid,newvalue){
//     console.log(`The ID is${theid}`)
//     console.log(`The newvalue is${newvalue}`)
//     document.getElementById("#table1_header").setAttribute("value", newvalue);
//     document.getElementById("#table1_header").textContent = newvalue;
// }

// function to change the html naming convenstion to more human appealing font
function formatname(nameinput){
    var converted_name = '';
    switch (nameinput){
        case "/ebitda_multiple":
            converted_name = "EBITDA Model";
            break;
        case "/ev_sales_multiple":
            converted_name = "EV Sales Model";
            break;
        case "/book_value_to_revenue_multiple":
            converted_name = "Book Sales to Revenue Model";
            break;
        case "/eps_multiple":
            converted_name = "EPS Model";
            break;
        case "/top_3":
            converted_name = "Top 3";
            break;
        case "/bottom_3":
            converted_name = "Bottom 3";
            break;

    }
    console.log(`PRINT CONVERTED NAME${converted_name}`)
    return converted_name;

}

function adddesc(modelname){
    console.log(modelname)
    endpoint = "/update_desc"
    let query_to_make = endpoint + modelname
    console.log(query_to_make)
    d3.json(query_to_make, function(data) {
        to_return = data[0].valuation_description
        console.log(to_return)
        document.getElementById("table1_header").setAttribute("title", to_return);
        return "updated header"
    });
}

// added event listener to table1 to update the value and text onces change is made
$(document).ready(function(){
    // init()
    $("#table1 li a").click(function(){
        multiple_to_display = $(this).attr("value");
        console.log(multiple_to_display);
        let current = document.getElementById("main_table").getAttribute('data-url');
        console.log(current);
        //changes the data url to new endpoint and update the table
        document.getElementById("main_table").setAttribute("data-url", multiple_to_display);
        $('#main_table').bootstrapTable('refresh',{"url":multiple_to_display});
        let current_table_value = document.getElementById("table1_header").getAttribute("value");
        //change text of header value
        document.getElementById("table1_header").setAttribute("value", multiple_to_display);
        // change the value of tool tip to reflect the text for the model
        adddesc(multiple_to_display)
        let formated_name = formatname(multiple_to_display);
        console.log(`Change Header to for table1 to ${formated_name}`);
        document.getElementById("table1_header").textContent = formated_name;
        //refresh the small table to reflect current model and update text for it
        document.getElementById("table2_header").setAttribute("value", "/top_3");
        document.getElementById("table2_header").textContent = "Top 3";
        // changetext(table1_header,formated_name);
        changesmalltable(multiple_to_display,'top_3');


    })


})

// added event listener to table2 to update the value and text onces change is made
$(document).ready(function(){
    // init()
    $("#table2 li a").click(function(){
        top_bottom = $(this).attr("value");
        console.log(top_bottom);
        document.getElementById("table2_header").setAttribute("value", top_bottom);
        let formated_name = formatname(top_bottom);
        console.log(`Change Header for table2 to ${formated_name}`);
        top_bottom = top_bottom.replace('/', '');
        console.log(top_bottom);
        let current_table_value = document.getElementById("table1_header").getAttribute("value");
        console.log(current_table_value);
        document.getElementById("table2_header").setAttribute("value", formated_name);
        document.getElementById("table2_header").textContent = formated_name;
        changesmalltable(current_table_value,top_bottom);

    })


})

adddesc('/eps_multiple')
