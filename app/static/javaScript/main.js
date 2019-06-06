$(document).ready(function () {

    $('body').append('<div id="grid"></div>')

    dataSource = new kendo.data.DataSource({
        transport: {
            // Get All Feature Requests 
            read: function (options) {
                $.ajax({
                    type: "GET",
                    url: "/requests",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    success: function (data) {
                        options.success(data);
                    }
                });
            },
            create: function (options) {
                // Creates A New Feature Request
                $.ajax({
                    type: "POST",
                    url: "/request/create",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    data: JSON.stringify(options.data.models[0]),
                    success: function (data) {
                        // Get All Feature Requests On Success
                        $("#grid").data("kendoGrid").dataSource.read();
                        options.success(data);
                    }
                });
            },
            update: function (options) {
                let ele = options.data.models[0]
                let data = {
                    id: ele.requestId, title: ele.title, description: ele.description,
                    target_date: ele.target_date, client_priority: ele.client_priority,
                    client_id: ele.client, product_area_id: ele.product_area
                }
                console.log(data)
                // Update A Spesfic Feature Requests
                $.ajax({
                    type: "PUT",
                    url: "/request/update",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    data: JSON.stringify(data),
                    success: function (data) {
                        // Get All Feature Requests On Success
                        $("#grid").data("kendoGrid").dataSource.read();
                        options.success(data);
                    }
                });
            },
            destroy: function (options) {
                // Delete A Spesfic Feature Requests
                $.ajax({
                    type: "DELETE",
                    url: "/request/delete",
                    contentType: "application/json; charset=utf-8",
                    dataType: 'json',
                    data: JSON.stringify(options.data.models[0].requestId),
                    success: function (data) {
                        // Get All Feature Requests On Success
                        $("#grid").data("kendoGrid").dataSource.read();
                        options.success(data);
                    }
                });
            },
        },
        batch: true,
        pageSize: 10,
        schema: {
            // Specify The Schema For the Add And Edit PopUp
            model: {
                id: "requestId",
                fields: {
                    title: { type: "string", validation: { required: true } },
                    description: { type: "string", validation: { required: true } },
                    target_date: { type: "date", validation: { required: true } },
                    client_priority: { type: "number", validation: { min: 1, required: true } },
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
            // Specify How The Data Will Be Shown
            { field: "requestId", title: "Id", width: 70 },
            { field: "title", title: "Title" },
            { field: "description", title: "Description" },
            { field: "target_date", title: "Target_date", template: '#= kendo.toString(kendo.parseDate(target_date), "dd/MM/yyyy")#' },
            { field: "client_priority", title: "Client_priority" },
            { field: "client", title: "Client", editor: clientDropDownEditor },
            { field: "product_area", title: "Product_area", editor: areaDropDownEditor },
            { command: ["edit", "destroy"], title: "&nbsp;" }
        ],

    });



});

EditPopup = (e) => {
    // Change The PopUp's Default Design
    $('.k-window-title').text("Feature Request");
    $('.k-grid-update').text("Save");
    $('.k-edit-field').first().remove();
    $('.k-edit-label').first().remove();
}

clientDropDownEditor = (container, options) => {
    // Create A DropDown List To Get The Clients Names/IDs From The DB
    $('<input required name="' + options.field + '"/>')
        .appendTo(container)
        .kendoDropDownList({
            autoBind: false,
            dataTextField: "name",
            dataValueField: "id",
            dataSource: {
                transport: {
                    read: "/clients"
                }
            }

        });
}
areaDropDownEditor = (container, options) => {
    // Create A DropDown List To Get The ProductAreas Names/IDs From The DB
    $('<input required name="' + options.field + '"/>')
        .appendTo(container)
        .kendoDropDownList({
            autoBind: false,
            dataTextField: "name",
            dataValueField: "id",
            dataSource: {
                transport: {
                    read: "/areas"
                }
            }

        });
}