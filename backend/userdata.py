from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
import json, os

#The user class, every user is stored as such in memory
class User(UserMixin):
    def __init__(self, email, username):
        self.id = email
        self.username = username


#Imports the user database into a dictionary
def import_usr_database():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, 'data', 'users.json')
    with open(path, 'r') as database:
            users = json.load(database)
            return users



#Creates an account and saves it to storage
def create_usr(email, usrname, password):
    base_dir = os.path.dirname(__file__)
    file = os.path.join(base_dir, 'data', 'users.json')
    with open(file, 'r') as database:
          change = json.load(database)
          if email in change:
               return False
          
    change[email] = {'username' : usrname , 'password' : generate_password_hash(password)}
    with open(file, 'w') as database:
         json.dump(change, database, indent=4)
    return True