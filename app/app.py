from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/album')
def album():
    return render_template("album.html")

@app.route('/auth')
def auth():
    return render_template("auth.html")


if __name__ == '__main__':
    app.run(debug=True)