
$(document).ready(function () {
    $("p").click(function () {
        event.preventDefault();
        var text = jQuery(this).text();
        text=text.replace("(","")
        var textList = text.split(",")
        insertDataForDelete(textList)
    });
});

function insertDataForDelete(textlist) {
    //selvitetään lista-alkioiden määrä ja luodaan for silmukalla + if-ehdolla yhtmä monta
    //html input kenttää kuin on alkioita.
    for (var i = 0; i <= textlist.length; i++) {
        if (i > 0) {
            var field = document.createElement("input")
            field.id = "field" + i
            field.name = "field" + i
            document.getElementById("crudArea").appendChild(field)

        }


    }
    document.getElementById("field1").value = textlist[0]
    document.getElementById("field2").value = textlist[1]
    var sendBtn = document.createElement("button")
    sendBtn.textContent = "Delete"
    document.getElementById("crudArea").appendChild(sendBtn)




}