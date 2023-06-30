from flask import Blueprint
#  router to where user can go

auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signin")
def signin():
    return "<p>SignIn</p>"
    



# @auth.route("/lol")
# def home():
