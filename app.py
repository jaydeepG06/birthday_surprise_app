from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/bronze")
def bronze():
    return render_template("bronze.html")

@app.route("/silver")
def silver():
    return render_template("silver.html")

@app.route("/gold")
def gold():
    return render_template("gold.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)