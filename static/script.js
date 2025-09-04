function createTextBox(cb) {
    console.log(cb)
    if (cb) {
        var textBox = document.createElement("textarea")
        var aiGenerate = document.createElement("button")
        aiGenerate.id = "aiBtn"
        aiGenerate.textContent = "Generate with AI"
        textBox.id = "tbox"
        document.getElementById("dataField").appendChild(textBox)
        document.getElementById("dataField").appendChild(aiGenerate)
    }
    if (cb === false) {
        document.getElementById("dataField").removeChild(document.getElementById("tbox"))
        document.getElementById("dataField").removeChild(document.getElementById("aiBtn"))

    }

}