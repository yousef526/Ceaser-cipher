#starting the app
from Ceaser_cipher import get_cipher
from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Welcome to Ceaser cipher Proejct</h1>'

@app.route('/encrypt',methods=['GET'])
def encrypt():
    # Get the 'data' query parameter
    data = request.args.get('params')
    
    # Parse the JSON string
    try:
        params = json.loads(data)
    except (TypeError, json.JSONDecodeError):
        return jsonify({"error": "Invalid JSON"}), 400
    
    
    msg = params.get('string')
    flag = params.get('encrypt')
    key = params.get('key')
    

    try:
        z = get_cipher(msg,flag,key)
        return jsonify({"result of encrypt":z})
    except ValueError:
        return jsonify({"error": "Invalid Data type"}), 400


@app.route('/decrypt',methods=['GET'])
def decrypt():
    data = request.args.get('params')
    print(data)
    try:
        params = json.loads(data)
    except (TypeError,json.JSONDecodeError):
        return jsonify({"error":"Wrong data type"}),400
    
    msg = params.get('string')
    flag = params.get('encrypt')
    key = params.get('key')
    

    try:
        z = get_cipher(msg,flag,key)
        return jsonify({"result of encrypt":z})
    except ValueError:
        return jsonify({"error": "Invalid Data type"}), 400





app.run(debug=True)