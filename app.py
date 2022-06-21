# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_recommend


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/results', methods = ['GET','POST'])
def results():
  if request.method == "POST":
    print(request.form["current"])
    user_current = request.form["current"]
    user_name = request.form["name"]
    user_major = request.form["major"]
    recommend = get_recommend(user_current,user_major)
    return render_template('results.html',user_current = user_current,user_name = user_name, user_major = user_major, recommend = recommend)
  else:
    return "error"