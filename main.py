import os
from fastapi import FastAPI, Form,Request,UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
from mongoconnection import DbConnection



load_dotenv() 

cbot=ChatBot('HistoryBot',storage_adapter='chatterbot.storage.SQLStorageAdapter', 
             database_uri='sqlite:///database.sqlite3',logic_adapters=["chatterbot.logic.TimeLogicAdapter"])


app=FastAPI()
dbConn=DbConnection()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

def listDirs():
     dirs=[]
     with os.scandir('C:\\') as entries:
        for entry in entries:
            #jos läpikäytä alkio on kansio lisätään se dirs listaan
            if entry.is_dir():
                #lisätään c:\ jokaisen kansion eteen
                dirs.append("C:\\"+entry.name)
            #huomaa että return on silmukan ulkopuolella, muuten silmukka tekisin vain yhden kierroksen
            #ja tallentaisi / palauttaisi vain yhden kansion.
        return dirs
     
     

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,} )

@app.get("/train",response_class=HTMLResponse)
def botTraining(request: Request):
    dirs=listDirs()
    return templates.TemplateResponse("trainBot.html", {"request": request,"dirs":dirs} )

@app.get("/createQuestion",response_class=HTMLResponse)
def createAiQuestion(request:Request):
    client = OpenAI(api_key=os.environ.get("apk"),)
    response = client.responses.create(
    model="gpt-4o",
    input="create history question with answer",)

    return templates.TemplateResponse("trainBot.html", {"request": request,"response":response.output_text} )

@app.post("/uploadDraggedFile",response_class=HTMLResponse)
async def uploadDraggedFile(inp:UploadFile):
     print(inp)
     

@app.post("/uploadFile",response_class=HTMLResponse)
async def uploadSelectedFile(file:UploadFile):
        file_path = os.getcwd()+"\\"+file.filename
        try:
            with open(file_path, "wb") as f:
                    f.write(file.file.read())
                    return"""
                            <html>
                                <head>
                                <title>Success</title>
                                </head>
                                <body>
                                <h1>Data successfully added to the bot</h1>
                                </body>
                            </html>
                            """
        except Exception as e:
            return {"message": e.args}
        
        
    
    

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

   
    

