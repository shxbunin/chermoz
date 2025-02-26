from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from userLogin import UserLogin
from database.tables import create_tables
from database.requests import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AFAFAFFAKFAMFJASNJGN23U4U284UGS'
# app.register_blueprint(app_route)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(int(user_id))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = get_user_by_email(request.form["username"])
        if user and check_password_hash(user.password, request.form["password"]):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect(url_for("index"))

    return render_template("login.html")

@app.route('/')
def index():
    user = get_user_by_id(int(current_user.get_id()))
    return render_template("index.html", user=user)

@app.route('/album')
@login_required
def album():
    return render_template("album.html")

def main():
    create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    main()