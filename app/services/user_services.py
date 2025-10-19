# app/services/user_service.py

from app import db
from app.models import User

def create_user(username, email, password):
    """Handles user registration logic."""
    if User.query.filter_by(email=email).first():
        return {"error": "User already exists"}, 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201


def get_user_by_email(email):
    """Fetch user details by email."""
    return User.query.filter_by(email=email).first()
