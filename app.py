# import dependency
from flask import Flask

# create Flask instance
app = Flask(__name__)

# create Flask routes
@app.route('/')

# define Flask route with a name. here its 
@app.route('/')
def hello_world():
    return 'Hello world'