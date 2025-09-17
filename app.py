import json
from flask import Flask, request, render_template, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from backend import mcserver, userdata

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
servers = {}
with open('config.json', 'r') as conf:
    config = json.load(conf)
app.secret_key = "some_long_random_string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/login_try', methods=['POST'])
def login_try():
    #Logins a user
    login = request.get_json()
    email = login.get("username")
    password = login.get("password")
    users = userdata.import_usr_database()
    if email not in users:
        return jsonify({"message": "Invalid Login"})
    elif check_password_hash(users[email]['password'], password):
        user = userdata.User(email, users[email]['username'])
        login_user(user)
        return jsonify({"message": "Valid Login, Welcome!"})
    else:
        return jsonify({"message": "Invalid Login"})
    
@app.route('/logout_try', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'logged out'})

@login_manager.user_loader
def load_user(user_id):
    users = userdata.import_usr_database()
    if user_id in users:
        return userdata.User(user_id, users[user_id]["username"])
    return None


@app.route('/start_server', methods=['POST'])
def start_server():
    servers[current_user.id] = mcserver.Server(f"{current_user.id}'s Server", current_user.id, 'jdk21')
    print("Server Object Initialized")
    servers[current_user.id].start(config)
    print('Server Starting')
    return jsonify({"message": "Server Starting!"})

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=config['web_port'])
    except Exception as e:
        print("Failed to run, did you install dependencies?")
        print(f"Error:\n{e}")
        input("Press enter to exit: ")