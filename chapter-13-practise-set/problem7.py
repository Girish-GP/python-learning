# explore flask module and create a web server

#🔹 Importing Flask: You're bringing in the Flask class from the flask module.
from flask import Flask

app = Flask(__name__)
#🔹 Creating an app instance:
# You’re creating a Flask web server object called app.
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses it to know where to look for resources like templates or static files.



@app.route('/')
def home():
    return "Hello , FLask!"
# 🔹 Route decorator:

# @app.route('/') tells Flask:
# 👉 “When someone accesses the root URL (like http://127.0.0.1:5000/), run the home() function.”

# 🔹 Function home():

# This function handles the request to / and returns the text 'Hello, Flask! 🚀'.

# This is what shows up in the browser.

@app.route('/test')
def test():
    return "This is test"

if __name__ == "__main__":
    app.run(debug=True)
#     🔹 Run the server only if this file is run directly (not imported elsewhere).

# 🔹 app.run(debug=True) starts the Flask development server:

# debug=True means:

# Auto-reload the server when you save the code.

# Show detailed error messages in the browser (useful during development).