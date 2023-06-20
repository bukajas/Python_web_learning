from flask import Blueprint
#  router to where user can go

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
