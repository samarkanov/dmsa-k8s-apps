from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    return '<h1 style=\"color:#FF6311;\">Simple</h1>'

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
