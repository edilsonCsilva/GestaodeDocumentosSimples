from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
app.debug=True

CORS(app)




@app.route("/")
def index():
	return 'Olá Mundo!  2021'

if __name__ == "__main__":
    
	app.run('0.0.0.0')