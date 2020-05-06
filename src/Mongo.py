import pymongo, os

class Mongo:
    def __init__(self, dbName, colName):
        try:
            mongoAddress = f"{os.environ['MONGO_HOST']}:{os.environ['MONGO_PORT']}"
        except:
            mongoAddress = "mongodb://localhost:27017/"
        print(f"Connecting to {mongoAddress}")
        myclient = pymongo.MongoClient(mongoAddress)
        mydb = myclient[dbName]
        self.mycol = mydb[colName]

    def __avoidDuplication(self, placa):
        if self.query({"placa": placa}).count() != 0:
            return False
        else:
            return True

    def insert(self, obj):
        if self.__avoidDuplication(obj.placa):
            x = self.mycol.insert(obj.__dict__)
            print(f"{obj.__dict__} object inserted")
            return x
        else:
            print(f"placa {obj.placa} duplicated")
            return {"status": "duplicated"}

    def query(self, myquery):
        #myquery = { "address": "Park Lane 38" }
        return self.mycol.find(myquery)