from flask import Blueprint, jsonify, request, render_template
from app.models.user import User
from app import db

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error" : "Missing data"}), 400

    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"Message":"User created successfully!"}), 201

@bp.route('/delete_user', methods=['DELETE'])
def delete_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"error": "Missing data"}), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error" : "User not found"}, 404)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"Message": f"User {username} deleted successfully!"}), 200