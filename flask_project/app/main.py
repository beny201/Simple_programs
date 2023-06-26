# File for your views

from flask import render_template, redirect, url_for, Blueprint, request, \
    session, flash
from . import db
from .models import Film, Opinion
from datetime import datetime

main_blueprint = Blueprint("main", __name__)
add_film_blueprint = Blueprint("add_film", __name__)
show_all_blueprint = Blueprint("show_all", __name__)
add_opinion_blueprint = Blueprint("add_opinion", __name__)


@main_blueprint.route('/', methods=["GET"])
def main():
    return render_template("index.html")


@add_film_blueprint.route('/add_film', methods=["POST", "GET"])
def add_film():
    if request.method == "POST":
        try:
            name = request.form['Name']
            creating_date_film = datetime.strptime(request.form['Date'],
                                                   "%Y-%m-%d")
            new_film = Film(name=name, date=creating_date_film)
            flash(f"{name} was added")
            db.session.add(new_film)
            db.session.commit()
        except ValueError as e:
            flash(f"{str(e)}")
            render_template("add_film.html")
    return render_template("add_film.html")


@show_all_blueprint.route('/show_all', methods=["GET"])
def show_all():
    all_film = Film.query.all()
    for film in all_film:
        print(film._id)
    all_opinion = Opinion.query.all()
    db.session.commit()

    for opinion in all_opinion:
        print(opinion.film_id)
    return render_template("show_films.html", films=all_film, opinions=all_opinion)


@add_opinion_blueprint.route('/add_opinion', methods=["POST", "GET"])
def add_opinion():
    if request.method == "POST":
        try:
            _id = request.form['film_id']
            opinion = request.form['opinion']
            found_film = Film.query.get(_id)
            new_opinion = Opinion(opinion=opinion, film_id=found_film._id)
            db.session.add(new_opinion)
            db.session.commit()
        except AttributeError as e:
            flash(f"{str(e)}")
            render_template("add_opinion.html")
    return render_template("add_opinion.html")
