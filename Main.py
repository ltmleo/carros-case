from src import Mongo, Carros

from flask import Flask, request, jsonify
from functools import wraps

db = Mongo.Mongo("carros", "carros")
app = Flask(__name__)

@app.route("/cadastrar",methods=["POST"])
def cadastrar():
    entrada = request.get_json()
    try:
        carro = Carros.Carros(entrada["Cor"], entrada["Placa"], entrada["Ano"], entrada["Modelo"])
    except ValueError:
        return jsonify({"status":"NOT OK","msg":"Valores Invalidos"})
    except KeyError:
        return jsonify({"status":"NOT OK","msg":"Chaves Invalidas"})
    print("Salvando na Base de Dados")
    try:
        inserted_id = db.insert(carro)
    except NameError:
        return jsonify({"status":"NOT OK","msg":f"Carro com a placa {carro.placa} Duplicado"})
    except:
        return jsonify({"status":"NOT OK","msg":"Algo de errado com a Base de Dados"})
    return jsonify({"status":"OK","ID":str(inserted_id)})

@app.route("/consulta/<chave>/")
@app.route("/consulta/<chave>/<valor>")
def consulta(chave, valor=""):
    consulta = {} if chave == "all" else {chave: valor}
    lista = []
    for i in db.query(consulta):
        lista.append({"placa": i["placa"], "cor": i["cor"], "modelo": i["modelo"], "ano": i["ano"]})
    return jsonify({"results": lista})

@app.route("/healthcheck")
def healthcheck():
    response = {"status":"OK 200"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)