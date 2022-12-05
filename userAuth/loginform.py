from flask import Blueprint, render_template

login = Blueprint("login", __name__)


@login.route("/loginform")
@login.route("/")
def log_in():
    return render_template("loginform.html")