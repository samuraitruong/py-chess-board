"""Waitress module"""
from app.main import api

def create_app():
    """factory method to create a flask app for waitress"""
    return api
