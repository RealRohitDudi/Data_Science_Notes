import main
import numpy as np
from flask import Flask,render_template,request
def get_ner():
    text = request.form.get("data")


    return render_template("home.html", result=response)