function showFilePrompt(cb) {
    console.log(cb)
    if (cb) {
        document.getElementById("filePromptDiv").hidden=false
    }
    else {
        document.getElementById("filePromptDiv").hidden=true

    }

}

var apk=""
function createAiQuestion() {
     $(function () {
    //haetaan apikey tekstitiedostosta
    jQuery.get('/static/apikey2.txt', function (data) {

        apk = data
        connectApi(apk)



    });
  })

  function connectApi(apk) {
      const API_URL="https://api.openai.com/v1/chat/completions"
    

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization":`Bearer ${apk}`
        },
        body:JSON.stringify({
            model:"gpt-3.5-turbo",
            messages:[{role: "user", content: "create short history question with answer"}]
        })


    }
    fetch(API_URL,requestOptions).then(res=>res.json()).then(data => {
        console.log(data)
        document.getElementById("tbox").value=data.choices[0].message.content

       
    }).catch((error)=>{
        console.log(error)
        
    })
}

  }

    
