from flask import Flask,render_template

enterance_quote = "This is the beginnig of Final"

website = Flask(__name__)
@website.route("/")
def subsite():
    int = 12 # I want to print this number on localhost
    str = "Final"
    dic = {"software" : "Python",5000 : "LocalHost :)"}
    return render_template("recap.html",number = int,str = str,title = enterance_quote,dic = dic) 
    # "number" is a key and it does not have to be "number"
    # input 

    
@website.route("/future")
def me():
    return """
     This is gonna be legend... 

     wait for it....

    daarryy :)
     
     """
if __name__ == "__main__":
    website.run(debug=True)
