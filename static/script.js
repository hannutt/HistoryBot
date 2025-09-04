function createTextBox(cb) {
    console.log(cb)
    if (cb) {
        document.getElementById("dataField").hidden=false
        document.getElementById("drop-zone").hidden=false
        var aiGenerate = document.createElement("button")
        aiGenerate.id = "aiBtn"
        aiGenerate.setAttribute("class","button-42")
        aiGenerate.textContent = "Generate with AI"
        document.getElementById("dataField").appendChild(aiGenerate)
        
    }
    if (cb === false) {
        document.getElementById("drop-zone").hidden=true
        document.getElementById("dataField").hidden=true
        document.getElementById("dataField").removeChild(document.getElementById("aiBtn"))

    }

}
const dropZone = document.getElementById("drop-zone");
const output = document.getElementById("output");

dropZone.addEventListener("drop", dropHandler);
window.addEventListener("dragover", (e) => {
  e.preventDefault();
});
window.addEventListener("drop", (e) => {
  e.preventDefault();
});
function dropHandler(ev) {
  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
  let result = "";
  // Use DataTransferItemList interface to access the file(s)
  [...ev.dataTransfer.items].forEach((item, i) => {
    // If dropped items aren't files, reject them
    if (item.kind === "file") {
      const file = item.getAsFile();
      result += `${file.name}\n`;
    }
  });
  output.textContent = result;
}
