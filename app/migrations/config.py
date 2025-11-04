from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def config_info(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mssql+pyodbc://@localhost/LaundryManagement?"
        "driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes&Encrypt=no"
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)