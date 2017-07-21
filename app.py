from flask import *
from random import *
app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def hello():
	if request.method == "GET":
		return render_template("bar.html")
	else:
		form= request.form
		name= form["Name"]
		email= form["Email"]
		message= form["Message"]
		print name +"_"+ email +"_"+ message
		return render_template("bar.html")



if __name__ =="__main__":
	app.run()