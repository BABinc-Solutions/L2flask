from flask import Blueprint, render_template

newusr = Blueprint("newusr", __name__)


@newusr.route("/newuserform")
@newusr.route("/")
def new_user():
    return render_template("newuserform.html")