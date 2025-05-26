from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_directory, 'app.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)