from flask import Flask, render_template, redirect, abort
app = Flask(__name__)

@app.route("/")
def index():
    name = " world"
    colour = "blue"
    return render_template("name.html",**locals())

@app.route("/people")
def people():
    return redirect("/people/George",302)

@app.route("/people/<string:name>/")
def get_person(name):
    if name != "George":
        return abort(403)
    colour = "red"
    return render_template("name.html",**locals())

if __name__ == "__main__":
    app.run(debug=True)