from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_users():
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"
    r = requests.get(url = URL)
    data = r.json()
    # return "Siema, wszystko działa poprawnie"
    print(data["joke"])
    return data

@app.route('/', methods=['GET'])
def test_enpoint():
    return "Serwis B działa poprawnie\nPowodzenia w dostaniu się do niego przez serwis A"

if __name__ == '__main__':
    app.run(debug=True)



