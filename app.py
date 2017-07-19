from flask import *
from random import *
app = Flask(__name__)
@app.route('/')
def hello():
	myList = ["Guitar","Piano","Violin"]
	display = True
	return render_template("bar.html",display=display,list=myList)

if __name__ =="__main__":
	app.run()