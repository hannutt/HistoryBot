import os
from fastapi import FastAPI, Form,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatterbot import ChatBot
chatbot = ChatBot("Historybot")

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,} )

@app.get("/train",response_class=HTMLResponse)
def botTraining(request: Request):
    return templates.TemplateResponse("trainBot.html", {"request": request,} )

@app.get("/readFile")
async def readFile(fpath:str):
    #path.split jakaa polun ja tiedostonnimen omiin osiin.
    file=os.path.split(fpath)
    print("data from file ",file[1])
    return  f'{fpath}'
    

