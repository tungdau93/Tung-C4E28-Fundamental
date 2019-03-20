from flask import Flask, render_template, redirect
import os
app = Flask(__name__)

@app.route("/about-me")
def ex1_study():
    info = {
        "name": "Đào Văn Tùng",
        "age": 25,
        "job": "7 job",
        "sex": "male",
        "address": "Hà Nội",
        "school": "FPT University",
        "hobbies": "Bóng đá, film, music"
    }
    return render_template("ex_study.html", info = info)
@app.route("/school")
def ex2_study():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)