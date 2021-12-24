#set up a flask and create a route - Mod 9.4.3


from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world, God is Great!'


