import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
mongoUser=os.environ.get("mongoUser")
mongoPsw=os.environ.get("mongoPsw")

class DbConnection():
      def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

      def connect(self):

        self.uri=f'mongodb+srv://{mongoUser}:{mongoPsw}@cluster0.gfnzlpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
                print(e)