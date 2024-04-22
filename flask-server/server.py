from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/members')
def members():
    return {"members":["mem1","mem2"]}

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)