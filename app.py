import pyrebase
from flask import *
import os

# ==== STUDY about HERE ==============
# https://rightcode.co.jp/blog/information-technology/flask-firebase-heroku-implementation-deploy


# ==== SetUp DataBase =================
#  Your web app's Firebase configuration
config = {
    "apiKey":os.environ['apikey'],
    "authDomain":os.environ['authDomain'],
    "databaseURL":os.environ['databaseURL'],
    "projectId":os.environ['projectId'],
    "storageBucket":os.environ['storageBucket'],
    "messagingSenderId":os.environ['messagingSenderId'],
    "appId":os.environ['appId'],
    "measurementId":os.environ['measurementId']
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
# ==== DataBase 書き込み ==================
# db.child("names").push({"name":"kata"})
# db.child("names").push({"name":"take"})
# ~ Error ~
# http://shinriyo.hateblo.jp/entry/2018/09/05/FirebaseのDBのパーミッションのエラー


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name = request.form['name']
            # Add and Get from DB
            if name:
                db.child("todo").push(name)
            todo = db.child("todo").get().val()

            if todo:
                return render_template('index.html', t=todo.values())
            else:
                pass
            
        elif request.form['submit'] == 'delete':
            db.child('todo').remove()
            return render_template('index.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
