from flask import Blueprint, jsonify
from .models import User
from . import db

bp = Blueprint('main', __name__)