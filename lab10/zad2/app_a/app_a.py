from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Adres URL aplikacji B
APP_B_URL = "http://service-b:3000"

@app.route('/proxy/jokes', methods=['GET'])
def proxy_get_jokes():
    url = f"{APP_B_URL}/jokes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), 200
    else:
        return jsonify({'error': 'Failed to fetch jokes from App B'}), 500
    
@app.route("/", methods=['GET'])
def hello():
    return "Goodbye world!"

@app.route('/proxy/messages', methods=['GET', 'POST'])
def proxy_messages():
    url = f"{APP_B_URL}/messages"
    if request.method == 'POST':
        message = request.json.get('message')
        if message:
            response = requests.post(url, json={'message': message})
        else:
            return jsonify({'error': 'Message field is required'}), 400
    else:
        response = requests.get(url)

    if response.status_code == 200:
        return response.json(), 200
    else:
        return jsonify({'error': 'Failed to fetch or add messages from/to App B'}), 500

@app.route('/proxy', methods=['GET'])
def test_proxy_endpoint():
    return "Proxy serwisu A do serwisu B działa poprawnie"

if __name__ == '__main__':
    app.run()
