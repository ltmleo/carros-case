from src import Mongo, Carros

db = Mongo.Mongo("carros", "carros")

carro = Carros.Carros("Branco", "GGF-2222", 2017, "HB20")

inserted_id = db.insert(carro)
print(f"inserted id: {inserted_id}")

for i in db.query({"cor": "Branco"}):
    print(f"oi {i}")