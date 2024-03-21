from flask import Flask, request, render_template, flash, redirect, url_for
from database import create_db, create_db_conn


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/add/")
def add_to_catalog():
    if request.method == "POST":
        name = request.form["name"]  # марка машини
        equipment = request.form["equipment"]  # модель
        top_speed = request.form["top_speed"]  # максимальна швидкість
        acceleration = request.form["acceleration"]  # розгін 0-100 км/год
        consumption = request.form["consumption"]  # витрата на 100 км
        weight = request.form["weight"]  # вага
        seats = request.form["seats"]  # к-ть мість + водій
        color = request.form["color"]  # кольори
        type_car = request.form["type_car"]  # тип кузова
        car = request.form["car"]  # фото автомобіля
        if not name:
            flash("Заповніть поле 'Назва'.")
        elif not equipment:
            flash("Заповніть поле 'Модель'.")
        elif not top_speed:
            flash("Заповніть поле 'Назва'.")
        elif not acceleration:
            flash("Заповніть поле 'Розгін'.")
        elif not consumption:
            flash("Заповніть поле 'Витрата'.")
        elif not weight:
            flash("Заповніть поле 'Вага'.")
        elif not seats:
            flash("Заповніть поле 'К-ть мість'.")
        elif not color:
            flash("Заповніть поле 'Кольори'.")
        elif not type_car:
            flash("Заповніть поле 'Тип кузова'.")
        elif not car:
            flash("Заповніть поле 'Фото авто'.")
        else:
            connection = create_db_conn()
            connection.execute("INSERT INTO catalog (name, equipment, top_speed, acceleration, consumption, weight, seats, color, type_car, car) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, equipment, top_speed, acceleration, consumption, weight, seats, color, type_car, car))
            connection.commit()
            connection.close()
            return redirect(url_for("main_page"))




app.run(port=36000, debug=True)