function createTextBox(cb) {
    console.log(cb)
    if (cb) {
        document.getElementById("tbox").hidden=false
        var aiGenerate = document.createElement("button")
        aiGenerate.id = "aiBtn"
        aiGenerate.setAttribute("class","button-42")
        aiGenerate.textContent = "Generate with AI"
        document.getElementById("dataField").appendChild(aiGenerate)
        
    }
    if (cb === false) {
        document.getElementById("tbox").hidden=true
        document.getElementById("dataField").removeChild(document.getElementById("aiBtn"))

    }

}