import os
from fastapi import FastAPI, Form,Request,UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from fastapi.responses import RedirectResponse
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
     
@app.get("/error",response_class=HTMLResponse)
def errPage(request:Request):
     return templates.TemplateResponse("error.html", {"request": request,} )
     

@app.get("/success",response_class=HTMLResponse)
def successPage(request:Request):
     return templates.TemplateResponse("success.html", {"request": request,} )
     
@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,} )

@app.get("/train",response_class=HTMLResponse)
def botTraining(request: Request):
    dirs=listDirs()
    return templates.TemplateResponse("trainBot.html", {"request": request,"dirs":dirs} )

     
@app.post("/uploadFile",response_class=HTMLResponse)
async def uploadSelectedFile(file:UploadFile):
        file_path = os.getcwd()+"\\"+file.filename
        file_path_str=str(file_path)
        try:
            with open(file_path, "wb") as f:
                    f.write(file.file.read())
            dataFile=open(file_path_str).read()
            print(dataFile)
            conversations = dataFile.strip().split('\n')
            trainer=ListTrainer(cbot)
            trainer.train(conversations)
            return RedirectResponse(url=f"/success/", status_code=200)
                            
        except: 
            return RedirectResponse(url=f"/error/", status_code=303)
        


@app.get("/readFile",response_class=HTMLResponse)
#fpath on samannimisen trainbot.html input kentän sisältö.
async def readFile(fpath:str):
    try:
        dataFile=open(fpath).read()
        conversations = dataFile.strip().split('\n')
        trainer=ListTrainer(cbot)
        trainer.train(conversations)
        return RedirectResponse(url=f"/success/", status_code=200)
    
    except:
         return RedirectResponse(url=f"/error/", status_code=303)
    


   
    

