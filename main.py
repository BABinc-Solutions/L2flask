from flask import Flask, render_template
from userAuth.signup import signup


app = Flask(__name__)
app.register_blueprint(signup, url_prefix="/userAuth")



@app.route("/")
def index():
    return render_template("login.html")


app.run(host="0.0.0.0", port=80)
