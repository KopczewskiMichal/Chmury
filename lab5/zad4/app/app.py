from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    print("Otrzymano żądanie")
    return 'Hello World'
 
if __name__ == '__main__':
    print("aplikacja się odpaliła")
    app.run(debug=True, port=3000)


