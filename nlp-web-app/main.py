from flask import Flask,render_template,request
import db
import features
app = Flask(__name__)
db1 = db.Database()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_login",methods=['POST'])
def perform_login():
    email = request.form.get("email")
    password = request.form.get("password")
    response = db1.search(email, password)
    if response == 404:
        print("user not found")
        return render_template("login.html", message="incorrect email or password")
    elif response == 200:
        print("login success")
        return render_template("home.html", message="logged in successfully")


@app.route("/perform_register",methods=['POST'])
def perform_register():
    name=request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("password")
    print("on backend, password is:",password)
    response = db1.create(email, name, password)
    if response == 200:
        print("user created successfully")
        return render_template("login.html",message="Registered Successfully, now login to continue.")
    elif response == 409:
       print("user already exists")
       return render_template("register.html", message="User already exists")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_ner",methods=['POST'])
features.get_ner()

app.run(debug=True)