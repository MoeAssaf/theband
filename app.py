from flask import *
from random import *
app = Flask(__name__)
@app.route('/')
def hello():
	return render_template("bar.html")


if __name__ =="__main__":
	app.run()