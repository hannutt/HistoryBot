import os
from fastapi import FastAPI, Form,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from openai import OpenAI

cbot=ChatBot('HistoryBot',storage_adapter='chatterbot.storage.SQLStorageAdapter', 
             database_uri='sqlite:///database.sqlite3',logic_adapters=["chatterbot.logic.TimeLogicAdapter"])

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,} )

@app.get("/train",response_class=HTMLResponse)
def botTraining(request: Request):
    return templates.TemplateResponse("trainBot.html", {"request": request,} )

@app.get("/readFile",response_class=HTMLResponse)
#fpath on samannimisen trainbot.html input kentän sisältö.
async def readFile(fpath:str):
    try:
        dataFile=open(fpath).read()
        conversations = dataFile.strip().split('\n')
        trainer=ListTrainer(cbot)
        trainer.train(conversations)
        return """
    <html>
        <head>
            <title>Success</title>
        </head>
        <body>
            <h1>Data successfully added to the bot</h1>
        </body>
    </html>
    """
    except:
        return """
    <html>
        <head>
            <title>Fail</title>
        </head>
        <body>
            <h1>Something went wrong.</h1>
        </body>
    </html>
    """

   
    

