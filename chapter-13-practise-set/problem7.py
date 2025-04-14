# explore flask module and create a web server

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello , FLask!"

if __name__ == "__main__":
    app.run(debug=True)