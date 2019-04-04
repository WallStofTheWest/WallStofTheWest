
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

function changesmalltable(current_table_value,top_bottom){
        let endpoint = "/top_bottom";
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

$(document).ready(function(){
    // init()
    $("#table1 li a").click(function(){
        multiple_to_display = $(this).attr("value");
        console.log(multiple_to_display);
        let current = document.getElementById("main_table").getAttribute('data-url');
        console.log(current);
        document.getElementById("main_table").setAttribute("data-url", multiple_to_display);
        $('#main_table').bootstrapTable('refresh',{"url":multiple_to_display});
        let current_table_value = document.getElementById("table1_header").getAttribute("value");
        document.getElementById("table1_header").setAttribute("value", multiple_to_display);
        let formated_name = formatname(multiple_to_display);
        console.log(`Change Header to for table1 to ${formated_name}`);
        
        document.getElementById("table1_header").textContent = formated_name;
        document.getElementById("table2_header").setAttribute("value", "/top_3");
        document.getElementById("table2_header").textContent = "Top 3";
        // changetext(table1_header,formated_name);
        changesmalltable(multiple_to_display,'top_3');

    
    })
    

})


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
