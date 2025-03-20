from flask import Flask, render_template, request, redirect, url_for, jsonify, Response, abort
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from userLogin import UserLogin
from database.tables import create_tables
from database.requests import *
from files import save_file
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AFAFAFFAKFAMFJASNJGN23U4U284UGS'
# app.register_blueprint(app_route)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(int(user_id))

@app.route("/addSection", methods=["POST", "GET"])
def addSection():
    if not current_user.is_authenticated or not current_user.admin:
        abort(403)
    if request.method == "POST":
        add_section(request.form["popup-title"], request.form["popup-desc"])

    return jsonify({'redirect': request.referrer or url_for('index')})

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if not current_user.is_authenticated or not current_user.admin:
        abort(403)
    if request.method == "POST":
        file = request.files["file"]
        img = file.read()
        add_photo(save_file(img, file.filename), int(request.form["album_id"]),
                  int(request.form["section_id1"]), request.form["popup-desc"])

    return jsonify({'redirect': request.referrer or url_for('index')})

@app.route("/addAlbum", methods=["POST", "GET"])
def addAlbum():
    if not current_user.is_authenticated or not current_user.admin:
        abort(403)
    if request.method == "POST":
        add_album(int(request.form["section_id2"]), request.form["popup-title"], request.form["popup-desc"])

    return jsonify({'redirect': request.referrer or url_for('index')})

@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = get_user_by_email(request.form["username"])
        if user and check_password_hash(user.password, request.form["password"]):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect(request.args.get("next") or url_for("index"))
        return redirect(url_for("login", next=request.args.get("next")))
    else:
        if current_user.is_authenticated:
            return redirect(request.args.get("next") or url_for("index"))
        return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    try:
        logout_user()
    except Exception as e:
        print(f"Login failed {e}")
    finally:
        return redirect(request.referrer)

        
    
@app.route('/')
def index():
    photos = get_recent_photos()
    return render_template("index.html", user=current_user, photos=photos)

@app.route('/album')
#@login_required
def album():
    sections = get_sections()
    sections.sort(key=lambda x: x.id)
    return render_template("album.html", user=current_user, sections=sections)

@app.route('/album/<int:id>')
def albums(id):
    albums = get_albums_by_section(id)
    photos = get_photos_by_section(id)
    return render_template("album-template.html", user=current_user, albums = albums, photos=photos)

@app.route('/photo/<int:id>')
def photo(id):
    photo = get_photo_by_id(id)
    return render_template("photo.html", user=current_user, photo=photo)

@app.route('/change_cover', methods=['POST'])
def change_cover():
    if not current_user.is_authenticated or not current_user.admin:
        return jsonify({'status': 'fail', 'result': f'You dont have the permission to access the requested resource'})
    data = request.get_json() or {}
    photo_id = data.get('id')
    change_album_cover(int(photo_id))
    return jsonify({'status': 'ok', 'result': f'Photo {photo_id} processed'})

@app.route('/delete_photo', methods=['POST'])
def delete_photo():
    if not current_user.is_authenticated or not current_user.admin:
        return jsonify({'status': 'fail', 'result': f'You dont have the permission to access the requested resource'})
    data = request.get_json() or {}
    photo_id = data.get('id')
    delete_photo_db(int(photo_id))
    return jsonify({'status': 'ok', 'result': f'Photo {photo_id} processed'})

@app.route('/edit_desc', methods=['POST'])
def edit_desc():
    if not current_user.is_authenticated or not current_user.admin:
        return jsonify({'status': 'fail', 'result': f'You dont have the permission to access the requested resource'})
    data = request.get_json() or {}
    photo_id = data.get('id')
    desc = data.get('desc')
    edit_photo_desc(int(photo_id), desc)
    return jsonify({'status': 'ok', 'result': f'Photo {photo_id} desc edited'})

def main():
    create_tables()
    app.run(debug=True)

if __name__ == '__main__':
    main()