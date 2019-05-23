$(document).ready(function () {

    $('body').append('<div id="grid"></div>')

    dataSource = new kendo.data.DataSource({
        transport: {
            read: function(options) {
                $.ajax({
                    type: "GET",
                    url: "/requests",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    success: function(data) {
                        options.success(data);
                    }
                });
            },
            create: function(options) {
                $.ajax({
                    type: "POST",
                    url: "/request/create",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    headers: {
                        "Access-Control-Allow-Origin":"*",
                        "Access-Control-Allow-Headers":"Content-Type, X-Requested-With, Origin, Accept",
                        "Access-Control-Allow-Methods":"GET, POST, PUT, DELETE, OPTIONS"
                    },
                    data: JSON.stringify(options.data.models[0]),
                    success: function(data) {
                        $("#grid").data("kendoGrid").dataSource.read(); 
                        options.success(data);
                    }
                });
            },
            update: function(options) {
                $.ajax({
                    type: "PUT",
                    url: "/request/update",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    headers: {
                        "Access-Control-Allow-Origin":"*",
                        "Access-Control-Allow-Headers":"Content-Type, X-Requested-With, Origin, Accept",
                        "Access-Control-Allow-Methods":"GET, POST, PUT, DELETE, OPTIONS"
                    },
                    data: JSON.stringify(options.data.models[0]),
                    success: function(data) {
                        $("#grid").data("kendoGrid").dataSource.read(); 
                        options.success(data);
                    }
                });
            },
            destroy: function(options) {
                $.ajax({
                    type: "DELETE",
                    url: "/request/delete",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    headers: {
                        "Access-Control-Allow-Origin":"*",
                        "Access-Control-Allow-Headers":"Content-Type, X-Requested-With, Origin, Accept",
                        "Access-Control-Allow-Methods":"GET, POST, PUT, DELETE, OPTIONS"
                    },
                    data: JSON.stringify(options.data.models[0]),
                    success: function(data) {
                        $("#grid").data("kendoGrid").dataSource.read(); 
                        options.success(data);
                    }
                });
            },
            parameterMap:  (options, operation) =>  {
                
                if (operation !== "read" && options.models) {
                    console.log(operation)
                    const data = options.models[0]
                    return data;
                }
            }
        },
        batch: true,
        pageSize: 10,
        schema: {
            model: {
                id: "FeatureID",
                fields: {
                    title: { type: "string", validation: { required: true } },
                    description: { type: "string", validation: { required: true } },
                    target_date: { type: "date", validation: { required: true } },
                    client_priority: { type: "number", validation: {min:1 , required: true } },
                    client: { type: "string", validation: { required: true } },
                    product_area: { type: "string", validation: { required: true } }
                }
            }
        }
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
            buttonCount: 5,
            pageSize: [5, 10, 20],
        },
        toolbar: ["create"],
        editable: "popup",
        edit: EditPopup,
        columns: [
            { field: "requestId", title: "Id", width:70 },
            { field: "title", title: "Title" },
            { field: "description", title: "Description" },
            { field: "target_date", title: "Target_date" },
            { field: "client_priority", title: "Client_priority" },
            { field: "client", title: "Client" },
            { field: "product_area", title: "Product_area" },
            { command: ["edit", "destroy"], title: "&nbsp;" }
        ],

    });



});

EditPopup = (e) => {
    if (e.model.isNew()) {
        $('.k-window-title').text("Feature Request");
        $('.k-grid-update').text("Save");
    }
        $('.k-edit-field').first().remove();
        $('.k-edit-label').first().remove();
}