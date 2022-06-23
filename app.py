from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("prediction.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Month"]

        Month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        name = request.form['name']
        if(name == 'jalsa'):
            jalsa = 1
            spiceelement = 0
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (name == 'spiceelement'):
            jalsa = 0
            spiceelement = 1
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (name == 'spiceelement'):
            jalsa = 0
            spiceelement = 1
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (name == 'bhagini'):
            jalsa = 0
            spiceelement = 0
            bhagini = 1
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (name == 'Grand_Village'):
            jalsa = 0
            spiceelement = 0
            bhagini = 0
            Grand_Village = 1
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (name == 'Izakaya_Gastro_Pub'):
            jalsa = 0
            spiceelement = 0
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 1
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 0

        elif (Name == 'Keys_Cafe_Keys_Hotel'):
            jalsa = 0
            spiceelement = 0
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 1
            Onesta = 0
            San_Churro_Cafe = 0

        elif (Name == 'Onesta'):
            jalsa = 0
            spiceelement = 0
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 1
            San_Churro_Cafe = 0

        elif (Name == 'San_Churro_Cafe'):
            jalsa = 0
            spiceelement = 0
            bhagini = 0
            Grand_Village = 0
            Izakaya_Gastro_Pub = 0
            Keys_Cafe_Keys_Hotel = 0
            Onesta = 0
            San_Churro_Cafe = 1

        location = request.form["Location"]
        if (Source == 'Banashankri'):
            Banashankari = 1
            Jayanagar = 0
            Kumaraswamy_Layout = 0

        elif (Source == 'Jayanagar'):
            Banashankari = 0
            Jayanagar = 1
            Kumaraswamy_Layout = 0

        elif(Source == 'Kumaraswamy Layout'):
            Banashankari = 0
            Jayanagar = 0
            Kumaraswamy_Layout = 1

        elif (Source == 'Banashankri'):
            Banashankari = 1
            Jayanagar = 0
            Kumaraswamy_Layout = 0

        cuisines = request.form["Cuisines"]
        if (cuisines == 'North Indian'):
            North_Indian = 1
            momos = 0
            singaporean = 0
            kashmiri = 0
            Pan_asian = 0
            d_Kolkata = 0

        elif (cuisines == 'momos'):
            North_Indian = 0
            momos = 1
            singaporean = 0
            kashmiri = 0
            Pan_asian = 0
            d_Kolkata = 0

        elif (cuisines == 'singaporean'):
            North_Indian = 0
            momos = 0
            singaporean = 1
            kashmiri = 0
            Pan_asian = 0
            d_Kolkata = 0

        elif (cuisines == 'kashmiri'):
            North_Indian = 0
            momos = 0
            singaporean = 0
            kashmiri = 1
            Pan_asian = 0

        elif (cuisines == 'Pan asian'):
            North_Indian = 0
            momos = 0
            singaporean = 0
            kashmiri = 0
            Pan_asian = 1

        prediction = model.predict([[
            jalsa,
            spiceelement,
            bhagini,
            Grand_Village,
            Izakaya_Gastro_Pub,
            Keys_Cafe-Keys_Hotel,
            Onesta,
            San_Churro_Cafe,
            Banashankari,
            Jayanagar,
            Kumaraswamy_Layout,
            North_Indian,
            momos,
            singaporean,
            kashmiri,
            Pan_asian

        ]])

        output = round(prediction[0], 2)

        return render_template('home.html', AMOUNT PREDICTED="Your Amount for this month needed is. {}".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
