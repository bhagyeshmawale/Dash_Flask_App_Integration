from flask import Flask,render_template,request
from datetime import datetime
import json



with open('config.json','r') as c:
	params=json.load(c)["params"]

local_Server = True

app = Flask (__name__)



@app.route("/")
def about():
	return render_template('about.html',params = params)


app.run(debug=True,port=8004)