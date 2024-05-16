from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_users():
    URL = "http://app_b:5002/joke"
    r = requests.get(url = URL)
    # data = r.json()
    # return data["joke"]
    return r


@app.route('/', methods=['GET'])
def test_enpoint():
    return "Server działa poprawnie.\nŻarty dostępne na endpointcie /jokes"

if __name__ == '__main__':
    app.run(debug=True)


# Z API tego mikroserwisku korzysta świat