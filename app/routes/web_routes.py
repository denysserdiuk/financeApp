from flask import Blueprint, jsonify, request, render_template

wp = Blueprint('main', __name__)


@wp.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@wp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@wp.route('/successful_registration', methods=['GET'])
def success_upon_registration():
    return render_template('successful_registration.html')