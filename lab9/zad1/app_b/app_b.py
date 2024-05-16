from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_users():
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"
    r = requests.get(url = URL)
    data = r.json()
    return data["joke"]


@app.route('/', methods=['GET'])
def test_enpoint():
    return "Server działa poprawnie.\nŻarty dostępne na endpointcie /jokes"

if __name__ == '__main__':
    app.run(debug=True)


# Z API tego mikroserwisu korzysta tylko mikroserwis a

