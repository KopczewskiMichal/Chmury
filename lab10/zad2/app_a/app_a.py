from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Adres URL aplikacji B
# APP_B_URL = "http://service-b:3000"
APP_B_URL = 'http://service-b.default.svc.cluster.local:3000'


@app.route('/proxy/jokes', methods=['GET'])
def proxy_get_jokes():
        try:
            url = f"{APP_B_URL}/jokes"
            response = requests.get(url, verify=False)
            app.logger.info(f"Connecting to {APP_B_URL}/jokes")
            
            if response.status_code == 200:
                app.logger.info(f"Received successful response from {APP_B_URL}/jokes")
                return response.json(), 200
            else:
                app.logger.error(f"Failed to fetch jokes from App B. Status code: {response.status_code}")
                return jsonify({'error': 'Failed to fetch jokes from App B'}), 500

        except requests.exceptions.RequestException as e:
            app.logger.error(f"RequestException: {str(e)}")
            return jsonify({'error': 'Failed to connect to App B'}), 500

        except socket.gaierror as e:
            app.logger.error(f"Socket gaierror: {str(e)}")
            return jsonify({'error': 'Failed to resolve host "service-b"'}), 500
    
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
