from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Group this is workshop 2, test finally working!'
