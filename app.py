from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')

@app.route('/update', methods=['POST'])
def update():
    os.system('cd /home/sakharovs/sakhar-site/python_website && git pull')
    os.system('touch /var/www/sakharovs_pythonanywhere_com_wsgi.py')
    return 'Updated via GitHub webhook', 200

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__=="__main__":
    app.run(debug=True)


