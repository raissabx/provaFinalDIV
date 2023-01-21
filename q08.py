from flask import Flask, request


app = Flask(__name__)

numero= {'numero': 0}

@app.route('/contador', methods=['POST']) 
def novo_numero():
    dado= request.json
    numero['numero'] = dado['numero']
    return {'numero': numero['numero']}, 201

@app.route('/contador', methods=['GET']) 
def leitura_numero():
    return {'numero': numero['numero']}, 200


@app.route('/contador/incrementa', methods=['PUT']) 
def incrementa_numero():
    numero['numero'] += 1
    return {'numero': numero['numero']}, 202


@app.route('/contador', methods=['DELETE']) 
def deleta_numero():
    numero['numero'] = 0
    return {'numero': numero['numero']}, 202

if __name__ == '__main__':
    app.run(debug=True)










