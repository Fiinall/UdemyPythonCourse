from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost" # If this programme is going to run on another host(cloud or rental host), 
                                       #its adress has to written here
app.config["MYSQL_USER"]        = "root" # Default value
app.config["MYSQL_PASWORD"]     = ""     # Default value
app.config["MYSQL_DB"]          = "final_database"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app) # Sets relationship btw MySQL & Flask

# Creating User Registration Form
class RegisterForm(Form):
    name = StringField("Name & Surname",validators = [validators.Length(min = 2,max = 30)])
    username = StringField("Username",validators = [validators.Length(min = 4,max = 15)])
    email = StringField("E-mail Adress",validators = [validators.Email(message = "Please enter a valid E-mail adress")])
    password = PasswordField("Password",validators = [
        validators.DataRequired("Please designate a password"),
        validators.EqualTo(fieldname = "confirm",message = "Passoword does not match")])
    confirm = PasswordField("Confirm Password")


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

# Register (Log In)
@app.route("/register")
def register():
    return render_template("final_register.html")
    


if __name__ == "__main__":
    app.run(debug=True)

