from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
@app.route("/")
def fatih():
    list = [1,2,10,"Fatih","Python"]
    global_value = "Udemy Course"
    info = [
        {"id" : 1,"Name":"Fatih","Age":22,"platform":global_value},
        {"id" : 2,"Name":"Name2","Age":2,"platform":global_value},
        {"id" : 3,"Name":"Name3","Age":3,"platform":global_value},
        {"id" : 4,"Name":"Name4","Age":4,"platform":global_value}
    ]
    return render_template("final_index.html",condition = 1,list = list,info = info)

@app.route("/about")
def about():
    return render_template("final_about.html")

@app.route("/materials/<string:number>")
def material(number):
    return "Number of material  " + number



if __name__ == "__main__":
    app.run(debug=True)

