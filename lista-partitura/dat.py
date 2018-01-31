import os
from flask import Flask, request, render_template,json ,jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/partituras', methods = ['GET'])
def getPartituras():
    p = open('datos.json', 'r')
    pString = json.load(p)
    return jsonify(pString)

@app.route('/status/')
def estadoOk():
    return jsonify({'status':'OK'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
