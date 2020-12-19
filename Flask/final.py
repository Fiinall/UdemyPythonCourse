from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "final"
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="Fatihinal",
    password="finaldatabase1",
    hostname="Fatihinal.mysql.pythonanywhere-services.com",
    databasename="Fatihinal$finaldatabase",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# In document it was "db = SQLAlchemy(app) but I'm changing it to yield my code"
mysql = SQLAlchemy(app)

"""
app.config["MYSQL_HOST"] = "localhost" # If this programme is going to run on another host(cloud or rental host), 
                                       #its adress has to written here
app.config["MYSQL_USER"]        = "root" # Default value
app.config["MYSQL_PASWORD"]     = ""     # Default value
app.config["MYSQL_DB"]          = "final_database"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app) # Sets relationship btw MySQL & Flask
"""
# User log in decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session: # The situation that session is begun.
            # If above is True, it means a user logged in. Dashboard is allowed to show up.
            return f(*args, **kwargs) # Calls dashboard when logged in
        else: # The sitation that session is not begun.
            flash ("To view this page, please log in","info")
            return redirect(url_for("login"))
    return decorated_function 
        


# Creating User Registration Form
class RegisterForm(Form):
    name = StringField("Name & Surname",validators = [validators.Length(min = 2,max = 30)])
    username = StringField("Username",validators = [validators.Length(min = 4,max = 15)])
    email = StringField("E-mail Adress",validators = [validators.Email(message = "Please enter a valid E-mail adress")])
    password = PasswordField("Password",validators = [
        validators.DataRequired("Please designate a password"),
        validators.EqualTo(fieldname = "confirm",message = "Passoword does not match")])
    confirm = PasswordField("Confirm Password")
    quizline = StringField("Let's apply what I learnt ; Just write your name again",validators = [validators.DataRequired("Nope! can't leave empty"),validators.EqualTo(fieldname = "name",message = "Olmadi canim")])

# User Log In Form
class LoginForm(Form):
    username = StringField("Username")
    password = PasswordField("Password")

@app.route("/")
def home():
    list = [1,2,10,"Fatih","Python"]
    global_value = "Udemy Course"
    info = [
        {"id" : 1,"Name":"Fatih","Age":22,"platform":global_value},
        {"id" : 2,"Name":"Name2","Age":2,"platform":global_value},
        {"id" : 3,"Name":"Name3","Age":3,"platform":global_value},
        {"id" : 4,"Name":"Name4","Age":4,"platform":global_value}
    ]
    return render_template("final_index.html",condition = 1,list = list,info = info)


@app.route("/dashboard")
@login_required # Just before 'dashboard' is run, loging_required will be run, session will be checked
                # If session is started, 'dashboard will be run, else log in page will be shown 
def dashboard(): 
    cursor = mysql.connection.cursor()
    query = "Select * From articles where author = %s"
    result = cursor.execute(query,(session["username"],))
    if result > 0: # If there are any articles belongs current user
        articles = cursor.fetchall()
        return render_template("final_dashboard.html",articles = articles)
    else:
        return render_template("final_dashboard.html")

@app.route("/about")
def about():
    return render_template("final_about.html")

@app.route("/materials/<string:number>")
def material(number):
    return "Number of material  " + number

#Article Detail Page. 
@app.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    query = "Select * From articles where id = %s"
    result = cursor.execute(query,(id,))

    if result > 0:
        article = cursor.fetchone() # We are going to select a certain article. Its id is primary so there is each articles id is different
        return render_template("final_article.html",article = article) 
    else: # result = 0 --> It means user has no article
        return render_template("final_article.html")



# Register (Log In)
@app.route("/register",methods =["GET","POST"])
def register():
    register_form = RegisterForm(request.form)
    if request.method == "POST" and register_form.validate():
        name = register_form.name.data
        username = register_form.username.data
        email = register_form.email.data
        password = sha256_crypt.encrypt(register_form.password.data)
        #quizline = register_form.quizline.data
        #-----------To see easier---------#
        cursor = mysql.connection.cursor()
        query = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Registration completed succesfully","success")
        return redirect(url_for("login"))
    else:
        return render_template("final_register.html",form = register_form)

@app.route("/login",methods = ["GET","POST"])
def login():
    login_form = LoginForm(request.form)
    if request.method =="POST":
        username = login_form.username.data
        password_entered = login_form.password.data # Password appear directly, not as ****** !!
        #-----------To see easier---------#
        cursor = mysql.connection.cursor()
        query = "Select * From users where username = %s"
        result = cursor.execute(query,(username,)) # Here, 'tuple' is needed!
                                                   # (something,) the "," at the end means
                                                   # it is a single element 'tuple' !!
        # is there is no username as input --> result would be "0"
        if result > 0 :
            data = cursor.fetchone() # Gives all informations about entered user, as dictionary
            password_real = data["password"] # Pick real password of that user. 
                                             # But it is encrypted!
            if sha256_crypt.verify(password_entered,password_real): # Cheks wheather entered password true.
                
                session["logged_in"] = True 
                session["username"] = username                                                   # If this statment returns True --> Successful log in
                flash("Log in is successful","success")
                return redirect(url_for("home"))
            else :
                flash("Incorrect Password","danger")
                return redirect(url_for("login"))

        else:
            flash("Invalid Username! Please try again.","danger")
            return redirect(url_for("login"))
                                          
        
    return render_template("final_login.html",form = login_form)

# logging out
@app.route("/logout")
def logout():
    session.clear() # kills the session
    flash("Logging out successfully","info")
    return redirect(url_for("home"))

# Updating Articles
@app.route("/update/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):
    if request.method == "GET":
        
        cursor = mysql.connection.cursor()
        query = "Select * From articles where author = %s and id = %s"
        result = cursor.execute(query,(session["username"],id))
        # If this result returns 0 ==> This can mean 2 situation
        # 1. The logged in user does not have any article
        # 2. The choosen article does not belong to logged in user.
        
        if result == 0  : 
            flash("Stated article does not exist or you don't have authority to make change!","danger")
            return redirect(url_for("dashboard"))

        else:
            article = cursor.fetchone() # Article has been called from database. Now title and contenc of article are obtained.
            # Now we need editing form again to change the article
            article_form = ArticleForm() # Normally there is request.from inside the paranthesis. The instructos says, the reason why there is not request.form there is to change the article not create a new one.
            article_form.title.data = article["title"]
            article_form.content.data = article["content"]
            return render_template("final_update.html",article_form = article_form)
            
    else : 
        # Here is 'POST' request part. Posting the editted article to database. 
        Article_form = ArticleForm(request.form)
        newtitle = Article_form.title.data
        newcontent = Article_form.content.data
        query2 = "Update articles Set title = %s, content = %s where id = %s" 
        cursor = mysql.connection.cursor()
        cursor.execute(query2,(newtitle,newcontent,id))
        mysql.connection.commit()
        flash("Article updated successfully","success")
        return redirect(url_for("dashboard"))
        
        
"""
@app.route("/update/<string:id>",methods = ["POST"])
@login_required
def update2(id):
    pass
    
"""        




# Article Deleting
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    query = "Select * From articles where author = %s and id = %s"
    result = cursor.execute(query,(session["username"],id))
    if result > 0:
        query2 = "Delete From articles where id = %s"
        cursor.execute(query2,(id,))
        mysql.connection.commit()
        return redirect(url_for("dashboard"))

    else:
        flash("Stated article does not exist or you don't have authority to make change!","danger")
        return redirect(url_for("home"))

# Article form
class ArticleForm(Form):
    title = StringField("Article Title",validators = [validators.Length(min = 2,max = 100)])
    content = TextAreaField("Article Content",validators = [validators.Length(min = 10)]) # Article has to has more area than other string inputs.

@app.route("/addarticle",methods =["GET","POST"])
def addarticle():
    article_form = ArticleForm(request.form)
    if request.method == "POST" and article_form.validate(): # If request is POST and validators are supplied
        title = article_form.title.data
        content = article_form.content.data
        #-----------To see easier---------#
        cursor = mysql.connection.cursor()
        query = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(query,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()
        flash("Article added succesfully","success")
        return redirect(url_for("dashboard"))       
    return render_template("final_addarticle.html",form = article_form)

@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    query = "Select * From articles"
    result = cursor.execute(query) # If there is no articles in database 'result' is going to be 0
    if result > 0 : # If there is one or more than one articles in database
        articles = cursor.fetchall() # returns all articles as 'dictionary in list'
        return render_template("final_articles.html",articles = articles)
    else:
        return render_template("final_articles.hmtl")

#Search URL
@app.route('/search', methods = ["POST"] )
def search():
    searching = request.form.get("keyword") # request.form = the informations from form, then get "keyword". "keyword" is the name of what is being searched.
    cursor = mysql.connection.cursor()
    print("---")
    print(type(searching))
    query = "Select * From articles where title like '%"+searching+"%'"
    result = cursor.execute(query)
    if result == 0:
        flash("There is no article including searched keyword","warning") # Try to print the keyword in this flash massage
        return redirect(url_for("articles"))
    elif result > 0:
        articles = cursor.fetchall()
        return(render_template("final_articles.html", articles = articles))

@app.route('/search',methods = ["GET"])
def search_get():
   return redirect(url_for("articles"))






if __name__ == "__main__":
    app.run(debug=True)

