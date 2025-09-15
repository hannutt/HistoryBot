function showFilePrompt(cb) {
    if (cb) {
        document.getElementById("filePromptDiv").hidden = false
    }
    else {
        document.getElementById("filePromptDiv").hidden = true

    }

}

function showFileUpload(cb) {
    if (cb) {
        document.getElementById("fileUpload").hidden = false
    }
    else {
        document.getElementById("fileUpload").hidden = true

    }

}
function showRestApi(cb) {
    if (cb) {
        document.getElementById("restapi").hidden = false
    }
    else {
        document.getElementById("restapi").hidden = true

    }

}
function showParse(cb) {
    if (cb) {
        document.getElementById("parse").hidden = false
    }
    else {
        document.getElementById("parse").hidden = true

    }

}
function selectLanguage() {
    var selectElement=document.getElementById("languages")
    var selectedLang = selectElement.value
    console.log(selectedLang)
    return selectedLang

}

function speak() {
    var speakLang=selectLanguage()
    var textToSpeech = document.getElementById("botAnswer").innerText
    var speechSynth = window.speechSynthesis;
    var newUtter = new SpeechSynthesisUtterance(textToSpeech);
    newUtter.lang=speakLang
    speechSynth.speak(newUtter);
    

}



function createAiQuestion() {
    $(function () {
        //haetaan apikey tekstitiedostosta
        jQuery.get('/static/apikey2.txt', function (data) {

            var apk = data
            connectApi(apk)
        });
    })
}

function connectApi(apk) {
    const API_URL = "https://api.openai.com/v1/chat/completions"


    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${apk}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: "create short history question with answer" }]
        })


    }
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        console.log(data)
        document.getElementById("tbox").value = data.choices[0].message.content


    }).catch((error) => {
        console.log(error)

    })
}




