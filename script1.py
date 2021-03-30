from flask import Flask, render_template #render_template renders a html file in the templates folder

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/wind-direction/')
def windDirection():
    return render_template("wind-direction.html")

if __name__=="__main__":
    app.run(debug=True)