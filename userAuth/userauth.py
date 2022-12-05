from flask import Blueprint, render_template, request
import json

userauth = Blueprint("userauth", __name__)


@userauth.route('/userauth', methods=['POST', 'GET'])
@userauth.route("/")
def user_auth():
    uname = request.form['username']
    pwd = request.form['password']
    good_usr = False

    with open("users.json", "r+") as file:
        jsonfile = json.load(file)
        for user in jsonfile["users"]:
            if user["username"] == uname:
                good_usr = True
                if user["password"] == pwd:
                    # Need to build logged inform and return it here
                    return render_template("loginform.html", value="Signed in")

    if not good_usr:
        return render_template("loginform.html", value="Incorrect user name")
    else:
        return render_template("loginform.html", value="Incorrect password")
