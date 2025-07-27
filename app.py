from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')


@app.route('/update', methods=['POST'])
def webhook():
    import os
    from datetime import datetime

    with open("deploy.log", "a") as f:
        f.write(f"\n[{datetime.now()}] 🔄 Запуск git pull\n")
        result = os.popen('cd /home/sakharovs/sakhar-site/python_website && git pull').read()
        f.write(result + "\n")

    os.system('touch /var/www/sakharovs_pythonanywhere_com_wsgi.py')
    return '✅ Обновлено', 200


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


