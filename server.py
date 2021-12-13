from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "you will never know"

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
  
    return redirect("/results")

@app.route("/results")
def user_info():
    return render_template("results.html",name=session["name"],location=session["location"],language=session["language"],comments=session["comments"])

if __name__=="__main__":
	app.run(debug=True)