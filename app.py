from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or not sport:
        return render_template("error.html", name=name, sport=sport)
    return render_template("register.html", name=name, sport=sport) # f"Welcome, {request.form.get("name")} to {request.form.get("sport")}"