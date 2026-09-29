#SYSTEM LIBRARIES
from flask import Flask
from flask import render_template 

#MY LIBRARIES
from module import dbConfig
from module import dbLogic

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0" 
APP_PORT = 5000



@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza" : "",
        "visina" : ""
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        
        if data["teza"] and data["visina"]:
            data["itm"] = izracunaj_itm(float(data["visina"]),float(data["teza"]))
        prnit(data)
        
    return render_template("index.html", podatki = data)
    
def izracunaj_itm(visinaCm, tezaKg):
    itm = teza / (visinaCm/100) ** 2
    return render_template("index.html", podatki = data)
print("Hello world")
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)