from flask import Blueprint, render_template
from .models import Siswa

auth = Blueprint("auth", __name__)

@auth.route("/")
def login():
    return render_template("auth/login.html")

@auth.route("/beranda")
def beranda():
    datasiswa = Siswa.query.all()
    return render_template("login/beranda.html", datasiswa=datasiswa)
