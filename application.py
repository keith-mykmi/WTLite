import sys
sys.path.append('/home/site/wwwroot')

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():

    uri = "mongodb://wtl:ThC65b3JBYd1CaCYqPaNImOFb6fWj4wOFeH1eanTWhaM4MqaYdq6kaCMQXf6dQU8YQTYRUaUjshiVp59eHoFsw==@wtl.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    myclient = MongoClient(uri)

    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    
    x= mycol.find_one()


    return "Hello World: "+x['name']
