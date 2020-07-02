from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    no = 12
    no_2 = 20
    car = dict()
    car["Brand"] = "Mercedes - Benz"
    car["Serie"] = "GLA 200"
    car["Configuration"] = "AMG"





    return render_template("index.html",number = no, number_2 = no_2,car = car)


@app.route("/about")
def about():

    
    return "This is FİNAL"




if __name__ == "__main__" :

    app.run(debug=True)


