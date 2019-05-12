$(document).ready(function () {

    $('body').append('<div id="grid"></div>')

    dataSource = new kendo.data.DataSource({
        transport: {
            read: {
                url: "/requests",
                dataType: "json"
            }
        },
        batch: true,
    });

    $("#grid").kendoGrid({
        dataSource: dataSource,
        height: 700,
        sortable: true,
        reorderable: true,
        resizable: true,
        pageable: {
            refresh: true,
            pageSizes: true,
            buttonCount: 5
        },
        columns: [
            { field: "title", title: "Title" },
            { field: "description", title: "Description" },
            { field: "target_date", title: "Target_date" },
            { field: "client_priority", title: "Client_priority" },
            { field: "client", title: "Client" },
            { field: "product_area", title: "Product_area" },
        ],

    });



});


