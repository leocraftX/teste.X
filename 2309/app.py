from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key="ChaveSecreta"

def conectar_banco():
    user= "root"
    host= "localhost"
    database= "sistema_login"
    password = ""

    
    return conectar_banco


@app.route("/")
def login():
    return render_template("login.html")

