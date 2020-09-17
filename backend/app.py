from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    lnk = "http://127.0.0.1:5000/"
    return render_template("index.html", link=lnk)

@app.route('/student')
def student():
    return render_template("student.html")

@app.route('/tutor')
def tutor():
    return render_template("tutor.html")

def send():
    pass
if __name__ == "__main__":
    app.run()