from flask import Blueprint, render_template, request
import json

# need to create a check for if username and password are blank strings
# need to add hashing to the the password

signup = Blueprint("signup", __name__)


@signup.route('/signup', methods=['POST', 'GET'])
@signup.route("/")
def sign_up():
    uname = request.form['username']
    pwd = request.form['password']

    dictionary = {
        "username": uname,
        "password": pwd
    }

    with open("users.json", "r+") as file:
        jsonfile = json.load(file)
        for user in jsonfile["users"]:
            if user["username"] == uname:
                return render_template("newuserform.html", value="This username is taken!")
        jsonfile["users"].append(dictionary)
        file.seek(0)
        json.dump(jsonfile, file, indent=4)
        return render_template("newuserform.html", value="User created!")
