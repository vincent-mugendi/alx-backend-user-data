#!/usr/bin/env python3
"""
Module for authentication views
"""

import os
from api.v1.views import app_views
from flask import abort, jsonify, request
from api.v1.views.users import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_user():
    """Function to handle user login"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout_user():
    """Function to logout a user"""
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if not logout:
        return abort(404)
    return jsonify({}), 200
