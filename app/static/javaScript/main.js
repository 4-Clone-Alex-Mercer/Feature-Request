$(document).ready(function () {

    $('body').append('<div id="grid"></div>')

    dataSource = new kendo.data.DataSource({
        transport: {
            read: {
                url: "/requests",
                dataType: "json"
            },
            create: {
                url: "/request/create",
                type: "POST",
                dataType: "json"
            },
            update: {
                url: "/request/update",
                type: "PUT",
                dataType: "json"
            },
            destroy: {
                url: "/request/delete",
                type: "DELETE",
                dataType: "json"
            },
            parameterMap:  (options, operation) =>  {
                console.log(options.models)
                if (operation !== "read" && options.models) {
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
        $('.k-edit-field').first().remove();
        $('.k-edit-label').first().remove();
    }
}
