import os
import pathlib
from fastapi import FastAPI, Form,Request,UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv, dotenv_values
from mongoconnection import DbConnection
import pandas as pd
import sqlite3
load_dotenv() 

cbot=ChatBot('HistoryBot',storage_adapter='chatterbot.storage.SQLStorageAdapter', 
             database_uri='sqlite:///database.sqlite3')


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

#laskee statement taulun rivit
def countSql():
    connection_obj = sqlite3.connect('database.sqlite3')
    cursor_obj = connection_obj.cursor()
    sql="SELECT COUNT (*) FROM statement"
    cursor_obj.execute(sql)
    output=cursor_obj.fetchone()
    connection_obj.commit()
    connection_obj.close()
    return output

def selectTrainingData():
    connection_obj = sqlite3.connect('database.sqlite3')
    cursor_obj = connection_obj.cursor()
    sql="SELECT id, text FROM statement"
    cursor_obj.execute(sql)
    sentences=cursor_obj.fetchall()
    connection_obj.commit()
    connection_obj.close()
    return sentences
     
     

@app.get("/crud",response_class=HTMLResponse)
def showStatistics(request:Request):
     #[(43,)]
     #total=countSql()
     savedData=selectTrainingData()

     return templates.TemplateResponse("cruds.html",{"request":request,"savedData":savedData})

@app.get("/train",response_class=HTMLResponse)
def botTraining(request: Request):
   
    dirs=listDirs()
    return templates.TemplateResponse("trainBot.html", {"request": request,"dirs":dirs} )

 

@app.post("/uploadCsv",response_class=HTMLResponse)
async def uploadScvFile(request:Request,csvfile:UploadFile):
     file_path = os.getcwd()+"\\"+csvfile.filename
     with open(file_path, "wb") as f:
          #csvfile = pelkkä uploadatun tiedoston nimi
          f.write(csvfile.file.read())
          #filepath on polku ja tiedosto
     df = pd.read_csv(file_path,skipinitialspace=True)
     print(df.to_string()) 

     return templates.TemplateResponse("trainBot.html",{"request":request})

@app.post("/uploadFile",response_class=HTMLResponse)
async def uploadSelectedFile(request: Request,file:UploadFile):
        #sovelluksen polku, jonne uploadattu tiedosto talletetaan
        file_path = os.getcwd()+"\\"+file.filename
        #selvitetään tiedostopääte
        file_path_str=str(file_path)
        try:
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            dataFile=open(file_path_str).read()
            #strip poistaa välilyönnit tekstin edestä ja lopusta, split jakaa tekstin lista-alkioiksi
            #rivivaihdon kohdalta.
            conversations = dataFile.strip().split('\n')
            trainer=ListTrainer(cbot)
            trainer.train(conversations)
        except:
                return RedirectResponse(url=f"/error/", status_code=303)
        return templates.TemplateResponse("trainBot.html", {"request": request} )
        
        


@app.post("/readFile",response_class=HTMLResponse)
#fpath on samannimisen trainbot.html input kentän sisältö, parsefile on samanniminen checkbox
async def readFile(request: Request,fpath:str=Form(...),items:str=Form(...),parseFile:bool=Form(False)):
    itemList=items.split(",")

    #jos html-checkbox on valittu
    if parseFile:
        # tiedostopolku+tiedoston
        dataFile=open(fpath).read()
        #listan merkkien läpikäynti i on vuorollaan jokainen alkio
        for i in itemList:
             #korvataan listalla olevat sanat tekstistä tyhjällä.
             dataFile=dataFile.replace(i,"")
             
        conversations = dataFile.strip().split('\n')
        trainer=ListTrainer(cbot)
        trainer.train(conversations)
      
    else:
         dataFile=open(fpath).read()
         conversations = dataFile.strip().split('\n')
         trainer=ListTrainer(cbot)
         trainer.train(conversations)

    return templates.TemplateResponse("trainBot.html", {"request": request} )

@app.post("/chatting",response_class=HTMLResponse)
async def createAnswer(request:Request,userInput:str=Form(...)):
     response=cbot.get_response(userInput)
     return templates.TemplateResponse("index.html", {"request": request,"response":response} )

@app.post("/deleteData",response_class=HTMLResponse)
async def deleteData(request:Request,field1:str=Form()):
    sqlId=field1
    connection_obj = sqlite3.connect('database.sqlite3')
    cursor_obj = connection_obj.cursor()
    sql=f"DELETE FROM statement WHERE id={sqlId}"
    cursor_obj.execute(sql)
    connection_obj.commit()
    connection_obj.close()
    message=f"Data with id {sqlId} removed from database"
    return templates.TemplateResponse("success.html",{"request":request,"message":message})

@app.post("/editData",response_class=HTMLResponse)
async def editData(request:Request, field1:str=Form(...),field2:str=Form(2)):
     
     sqlId=field1
     sentence=field2
     connection_obj = sqlite3.connect('database.sqlite3')
     cursor_obj = connection_obj.cursor()
     sql="UPDATE statement SET text=? WHERE id=?"
     cursor_obj.execute(sql,(sentence,sqlId))
     connection_obj.commit()
     connection_obj.close()
     message=f"Data with id {sqlId} updated"
     return templates.TemplateResponse("success.html",{"request":request,"message":message})


         
    
    
    

          
    


   
    

