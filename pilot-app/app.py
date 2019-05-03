from flask import Flask, render_template, redirect, request, session
from services import service_collection
from bson.objectid import ObjectId
app = Flask(__name__)
app.config["SECRET_KEY"] = "93J#DJHDA&("

@app.route('/')
def index():
    if('logged' in session):
        if session["logged"] == True:
            return render_template('homepage.html')
        else:
            return redirect("/login")
    else:
        session['logged'] = False
        return redirect("/login")

@app.route('/all-service')
def data():
    if('logged' in session):
        if(session["logged"] == True):
            all_services = service_collection.find()
            return render_template("all-services.html", all_services = all_services)
        else:
            return redirect("/login")
    else:
        session['logged'] = False
        return redirect("/login")

@app.route('/all-service/<gender>')
def data_gender(gender):
    if(session["logged"] == True):
        gender_services = service_collection.find({"gender": gender})
        return render_template("all-services.html", all_services = gender_services)
    else:
        return redirect("/login")

@app.route('/all-service/detail/<id>')
def detail(id):
    if(session["logged"] == True):
        detail_services = service_collection.find_one({ "_id": ObjectId(id) })
        return render_template("detail.html", service = detail_services)
    else:
        return redirect("/login")

@app.route('/delete/<id>')
def delete(id):
    if(session["logged"] == True):
        delete_services = service_collection.find_one({ "_id": ObjectId(id) })
        if delete_services is not None:
            service_collection.delete_one(delete_services)
            return redirect("/all-service")
    else:
        return redirect("/login")

@app.route('/all-service/update/<id>', methods = ["GET", "POST"])
def update(id):
    if(session["logged"] == True):
        edit_services = service_collection.find_one({ "_id": ObjectId(id) })
        if(request.method == "GET"):
            return render_template("update.html", service = edit_services)
        elif(request.method == "POST"):
            form = request.form
            name = form["full_name"]
            age = form["age"]
            address = form["address"]
            gender = form["gender"]
            available = form["available"]
            new_value = {  "$set": { "name": name, "age": age, "address": address, "gender": gender, "available": available } }
            service_collection.update_one(edit_services, new_value)
            return redirect("/all-service/detail/{}".format(id))
    else:
        return redirect("/login")

@app.route('/login', methods = ["GET", "POST"])
def login():
    if('logged' in session):
        if(session["logged"] == False):
            if(request.method == "GET"):
                return render_template("login.html")
            elif(request.method == "POST"):
                form = request.form
                username = form["username"]
                password = form["password"]
                if(username == "tram" and password == "cho"):
                    session["logged"] = True
                    return redirect("/all-service")
                else:
                    return redirect("/login")
        else:
            return redirect("/all-service")
    else:
        session['logged'] = False
        return redirect('/login')

@app.route('/logout')
def logout():
    session["logged"] = False
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)