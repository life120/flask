from flask import Flask #importing the Flask class object

app = Flask(__name__) #when Python runs the main script(this script), it will auto-assign __name__ = "__main__". However, if you plan to run an imported script, then you must assign __name__ = "script2" 

@app.route('/') # / indicates the first page the website shows when script initiates. When the script is executed, it will run the main page first. So it will route over to @app.route('/') first
def home():
    return "Website content goes here!"

@app.route('/about/') #http://127.0.0.7:5000/about web page. To go here, you must input the /about/ at the end of the main page address to go to this page.
def about():
    return "About Page content goes here!"

if __name__=="__main__":            #this is the one that runs the page
    app.run(debug=True)