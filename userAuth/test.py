from flask import Blueprint, render_template, request
import json

test = Blueprint("test", __name__)


@test.route('/test', methods=['POST', 'GET'])
@test.route("/")
def test_test():
    uname = request.form['username']
    pwd = request.form['password']

    dictionary = {
        "username": uname,
        "password": pwd
    }

    show = []
    with open("users.json", "r+") as file:
        jsonfile = json.load(file)
        for user in jsonfile["users"]:
            if user["username"] == uname:
                return "This username is taken!"
        return "You have created a new user"
            #show = str(user["username"] + "<br>")


        # if str(uname) == str(jsonfile["users"][1]):
        #     return "This username is taken!"
        # elif uname != jsonfile["users"][1]:
        #     return "test " + uname + " " + str(jsonfile["users"][1]["username"])

