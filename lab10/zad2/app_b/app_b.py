from flask import Flask, jsonify, request
from pymongo import MongoClient
import requests

app = Flask(__name__)

# Połączenie z bazą danych MongoDB
client = MongoClient("mongodb://mongodb:27017/")  # adres hosta bazy danych
db = client["mydatabase"]
collection = db["messages"]

@app.route('/', methods=['GET'])
def get_jokes():
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"
    r = requests.get(url = URL)
    print(r)
    data = r.json()
    return data["joke"]

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        message = request.json.get('message')
        if message:
            collection.insert_one({'message': message})
            return jsonify({'message': 'Message added successfully'}), 201
        else:
            return jsonify({'error': 'Message field is required'}), 400
    elif request.method == 'GET':
        messages = list(collection.find({}, {'_id': 0}))  # pobierz wszystkie wiadomości
        return jsonify(messages)

@app.route('/', methods=['GET'])
def test_enpoint():
    return "Serwis B działa poprawnie\nPowodzenia w dostaniu się do niego przez serwis A"

if __name__ == '__main__':
    app.run(debug=True)
