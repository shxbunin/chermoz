from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from userLogin import UserLogin
from database.tables import create_tables
from database.requests import *
from files import save_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AFAFAFFAKFAMFJASNJGN23U4U284UGS'
# app.register_blueprint(app_route)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(int(user_id))

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        img = file.read()
        add_photo(save_file(img, file.filename))

    return redirect(url_for("index"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = get_user_by_email(request.form["username"])
        if user and check_password_hash(user.password, request.form["password"]):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect(url_for("index"))
    else:
        user = current_user.get_id()

        if user is not None:
            return redirect(url_for("index"))
     
        return render_template("login.html")
        
    
@app.route('/')
def index():
    user = current_user.get_id()
    if user is not None:
        user = get_user_by_id(int(current_user.get_id()))
    return render_template("index.html", user=user)

@app.route('/album')
#@login_required
def album():
    user = current_user.get_id()
    if user is not None:
        user = get_user_by_id(int(current_user.get_id()))
    return render_template("album.html", user=user)

def main():
    create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    main()