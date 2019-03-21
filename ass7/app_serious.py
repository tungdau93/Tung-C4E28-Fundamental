from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmiwithout/<int:weight>/<int:height>')
def ex_serious_without_templates(weight, height):
    BMI = weight/((height/100)**2)
    if(BMI < 16):
        return "Severely underweight"
    elif(BMI < 18.5):
        return "Underweight"
    elif(BMI < 25):
        return "Normal"
    elif(BMI < 30):
        return "Overweight"
    else:
        return "Obese"

@app.route('/bmiwith/<int:weight>/<int:height>')
def ex_serious_with_templates(weight, height):
    BMI = weight/((height/100)**2)
    return render_template("ex_serious.html", BMI = BMI)

if __name__ == '__main__':
    app.run(debug=True)
