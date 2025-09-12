
function createTextBox(cb) {
  console.log(cb)
  if (cb) {
    document.getElementById("dataField").hidden = false
  
    var aiGenerate = document.createElement("button")
    aiGenerate.id = "aiBtn"
    //aiGenerate.setAttribute("class", "button-42")
    aiGenerate.textContent = "Generate with AI"
    aiGenerate.addEventListener("click",createAiQuestion)
    document.getElementById("dataField").appendChild(aiGenerate)

  }
  if (cb === false) {
   
    document.getElementById("dataField").hidden = true
    document.getElementById("dataField").removeChild(document.getElementById("aiBtn"))

  }

}
/*
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
  fileInput.filename = files


}*/

var selected=""
function getSelectedOption(sel) {

  selected=document.getElementById("topics").value = sel.options[sel.selectedIndex].text
}

function startDate() {
  var sd = document.getElementById("startDate").value
  var startArray = sd.split("-")
  return startArray
}
function fetchData() {

  $(function () {
    //haetaan apikey tekstitiedostosta
    jQuery.get('/static/apikey.txt', function (data) {
      var apk = data
      connect(apk)
    });
  })
}

function connect(apk) {
  var dates = startDate()
  console.log(dates)
  var options = {
    method: 'GET',
    headers: { 'x-api-key': apk }
  }

  var url = `https://api.api-ninjas.com/v1/historicalevents?text=${selected}&year=${dates[0]}&month=${dates[1]}&day=${dates[2]}`


  fetch(url, options)
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data)
      //näytetään textareassa vain event-property eli tapahtumat, ei päivämääriä yms.
      //document.getElementById("apiText").value=data[0].event
    })
    .catch(err => {
      console.log(`error ${err}`)
    });
}

function listDirs() {
  var dirs = document.getElementById("dirs").innerText
  //pilkotaan kansiot , merkin kohdalta omiksi lista-alkioiksi dirArray listaan
  var dirArray = dirs.split(",")
  //poistetaan ' ja [ ] merkit listan alkioista. lista käydään läpi silmukassa, jolloin
  //kaikki löydetyt merkit poistetaan yhdellä kertaa.
  for (var i = 0; i < dirArray.length; i++) {

    dirArray[i] = dirArray[i].replace("'").replace("undefined", "").replace("'", "").replace("undefined", "'")
      .replace("[", "'").replace("]", "").replace("\\","")
    console.log(dirArray[i])
  }
  //palautetaan dirArray lista ja käytetään sitä allaolevassa jquery funktiossa.
  return dirArray
}

function autoCompleteText(cb) {
  if (cb) {
    $(document).ready(function () {
  $(function () {
    var availableTags = listDirs()

    $("#fpath").autocomplete({
      source: availableTags


    });
  });
})

  } if(cb===false) {
      $("#fpath").autocomplete({
            disabled: true
        });

    }
  }





