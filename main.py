from flask import Flask
server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Thank you!!'











server.run(host='0.0.0.0', debug=True)