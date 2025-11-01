from flask import Flask
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def hello_world():
    """Serves the home page."""
    return '<h1>Hello, World!</h1><p>Your Flask app is running.</p>'

# Define a second route
@app.route('/about')
def about():
    """Serves the 'about' page."""
    return '<h3>This is the about page.</h3>'

# This block is crucial for deployment
if __name__ == "__main__":
    # Get the port number from the environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app. 
    # '0.0.0.0' makes it accessible from any IP address (important for containers/VMs)
    app.run(host='0.0.0.0', port=port, debug=True)
