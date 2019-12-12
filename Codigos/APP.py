import datetime
from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from banco_de_dados import BancoDeDados
import json

app = Flask(__name__)
api = Api(app, version = "1.0", title = "Trabalho",
    description = "API")

ns = api.namespace("api", description = "Operacoes")
banco = BancoDeDados()


@ns.route("/ins_gas/<valor>")
class InsGas(Resource):
    def post(self, valor):
        return banco.ins_gas(valor)

@ns.route("/ins_humidade/<valor>")
class InsHumidade(Resource):
    def post(self, valor):
        return banco.ins_humidade(valor)

@ns.route("/inserir_temperatura/<valor>", methods = ["POST"])
class InsTemperatura(Resource):
    def post(self, valor):
        return banco.ins_temperatura(valor)


@ns.route("/selecionar/<humidade>/<temperatura>/<gas>/<de>/<ate>")
class Selecionar(Resource):
    def get(self, humidade, temperatura, gas, de, ate):
        if humidade == "False":
            humidade = False
        else:
            humidade = True

        if temperatura == "False":
            temperatura = False
        else:
            temperatura = True

        if gas == "False":
            gas = False
        else:
            gas = True

        dados, flag = banco.selecionar_dados(humidade, temperatura, gas, de, ate)

        if not dados:
            return 404

        media = 0
        if not flag:
            for i in dados:
                media += i[1]

            media = media / len(dados)
            dados.append(media)
        else:
            media_tem = 0
            media_hum = 0
            media_gas = 0

            for i in dados[1]:
                media_tem += i[-1]

            for i in dados[0]:
                media_hum += i[-1]

            for i in dados[2]:
                media_gas += i[-1]

            media_tem = media_tem / len(dados[1])
            media_hum = media_hum / len(dados[0])
            media_gas = media_gas / len(dados[2])

            dados.append(media_tem)
            dados.append(media_hum)
            dados.append(media_gas)

        return jsonify(dados)

if __name__ == "__main__":
    app.run("IP_MÁQUINA", debug = True)
