from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        print("WORKS")
        username = request.form["username"]
        password = request.form["password"]

        print(username, password)
        return redirect(url_for("index"))
    return render_template("names.html")


app.run(debug = True)
