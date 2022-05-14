from flask import Flask, render_template, request, redirect, url_for, Response
import config

app = Flask(__name__)
app.secret_key = config.secret_key


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    if request.method == "POST":
        zipCode = request.form['zipCode']
        print(zipCode)
        return render_template('results.html')






if __name__ == "__main__":
    app.run(debug=True)