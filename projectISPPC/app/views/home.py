from flask import Blueprint, render_template, redirect, request, url_for, flash

# from ..models.models import Usuario

home = Blueprint("home", __name__)

@home.route("/")
def index():
    return render_template("home.html")