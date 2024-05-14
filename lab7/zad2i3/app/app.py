from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/users?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    
    users_json = []
    for user in users:
        user_data = {
            'id': str(user['_id']),
            'username': user['username'],
            'email': user['email']
        }
        users_json.append(user_data)
    
    return jsonify(users_json)

@app.route('/', methods=['GET'])
def test_enpoint():
    return "Siema, działam"

if __name__ == '__main__':
    app.run(debug=True)


