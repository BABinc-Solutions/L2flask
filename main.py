import sys
from flask import Flask, render_template
from userAuth.signup import signup
from userAuth.newuserform import newusr

app = Flask(__name__)
app.register_blueprint(signup, url_prefix="/userAuth")
app.register_blueprint(newusr, url_prefix="/userAuth")

exit_main = False
try:

    debug_str = sys.argv[1]
    if debug_str.upper() == "FALSE":
        debug_bool = False
    elif debug_str.upper() == "TRUE":
        debug_bool = True
    else:
        exit_main = True
        raise Exception("You ran main.py with an incorrect argument.")
except:
    if exit_main:
        sys.exit("You ran main.py with an incorrect argument.")
    else:
        debug_bool = True


@app.route("/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", port=80, debug=debug_bool)
