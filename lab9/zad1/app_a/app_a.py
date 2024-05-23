from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/jokes', methods=['GET'])
def get_users():
    # URL = "http://127.0.0.1:5002/jokes"
    URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=political,racist,sexist&type=single"

    # URL = "http://service-b:30080/jokes"
    r = requests.get(url = URL)
    print(r)
    data = r.json()
    
    print(data["joke"], "!!!!!!!!!")
    return data["joke"]
    # return r


@app.route('/', methods=['GET'])
def test_enpoint():
    return "Server działa poprawnie!\nŻarty dostępne na endpointcie /jokes"

@app.route('/internal', methods=['GET'])
def internalRequest():
    # URL = "http://127.0.0.1:5002/"
    URL = "http://service-b:5002/"

    r = requests.get(url = URL)
    # data = r.json()
    # return data["joke"]
    print(r)
    return r

if __name__ == '__main__':
    app.run(debug=True)


#* Z API tego mikroserwisku korzysta świat

# TODO: chyba chce wyprintować wynik
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/app/app_a.py", line 14, in get_users
#     print(data["joke"])