from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_jokes():
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"
    r = requests.get(url = URL)
    print(r)
    data = r.json()
    return data["joke"]

@app.route('/', methods=['GET'])
def test_enpoint():
    return "Serwis B działa poprawnie\nPowodzenia w dostaniu się do niego przez serwis A"

if __name__ == '__main__':
    app.run(debug=True)


