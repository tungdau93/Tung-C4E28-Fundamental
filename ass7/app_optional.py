from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    users = {
        "tung": {
                    "name": "Đào Văn Tùng",
                    "age": 26,
                    "sex": "male",
                    "hobbies": "football, music"
                },
        "tram": {
                    "name": "Trần Thị Trâm",
                    "age": 20,
                    "sex": "female",
                    "hobbies": "football, music, book"
                },
        "hoabinh": {
                    "name": "Đào Trần Hòa Bình",
                    "age": 6,
                    "sex": "male",
                    "hobbies": "football, music, game"
                }
    }
    return render_template('ex_optional.html', username = username, users = users)

if __name__ == '__main__':
    app.run(debug=True)
 