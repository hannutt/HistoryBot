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
const fileInput = document.getElementById("fileInput")
var files;
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
  //raahatun tiedoston nimi
  files = ev.dataTransfer.files;
  
  // Use DataTransferItemList interface to access the file(s)
  [...ev.dataTransfer.items].forEach((item, i) => {
    // If dropped items aren't files, reject them
    if (item.kind === "file") {
      const file = item.getAsFile();
      result += `${file.name}\n`;
    }
  });
  output.textContent = result;
  fileInput.filename=files
  

}
function listDirs() {
 
  var dirs=document.getElementById("dirs").innerText
  //pilkotaan kansiot , merkin kohdalta omiksi lista-alkioiksi dirArray listaan
  var dirArray=dirs.split(",")
  //poistetaan ' ja [ ] merkit listan alkioista. lista käydään läpi silmukassa, jolloin
  //kaikki löydetyt merkit poistetaan yhdellä kertaa.
  for ( var i=0; i<dirArray.length;i++) {

    dirArray[i]=dirArray[i].replace("'").replace("undefined","").replace("'","").replace("undefined","'")
    .replace("[","'").replace("]","")
    console.log(dirArray[i])
  }
    //palautetaan dirArray lista ja käytetään sitä allaolevassa jquery funktiossa.
  return dirArray
}
$(document).ready(function(){
 $( function() {
    var availableTags = listDirs()

    $( "#fpath" ).autocomplete({
      source: availableTags
    
    
    });
  });
})

