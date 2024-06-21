from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_users():
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"
    r = requests.get(url = URL)
    print(r)
    data = r.json()
    
    return data["joke"]
    # return r


@app.route('/', methods=['GET'])
def test_enpoint():
    return "Server działa poprawnie!\nŻarty dostępne na endpointcie /jokes"

@app.route('/internal', methods=['GET'])
def internal_request():
    URL = "http://service-b:5002/jokes"
    r = requests.get(url=URL)
    return r.text


if __name__ == '__main__':
    app.run(debug=True)


#* Z API tego mikroserwisku korzysta świat
