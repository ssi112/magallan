"""
routes.py - maps URLs to functions

"""
from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm
#from flask_session import Session

# ORG CODE from models import db

app = Flask(__name__)

app.secret_key = "A00r69j/3yX R~XhH!jmN]L_X/M?rT"


# ORG CODE app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
# ORG CODE db.init_app(app)

# --------------------------------------------------
from models import Base, User
import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import exc # exception

# Create an engine that stores data in the local db file
# engine = create_engine('postgresql://USER:PW@localhost:5432//learningflask')
try:
    engine = create_engine(connection.db_connect)
    print("*** INSIDE ROUTES.PY ***")
    print(connection.db_connect)
except exc.SQLAlchemyError:
    print("\n *** Oh crap. Something went wrong! *** \n")


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
dbSession = DBSession()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    session['tmp'] = "more session crap"
    return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form = form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            dbSession.add(newuser)
            dbSession.commit()
            # create new session for user that just signed up
            session['email'] = newuser.email
            # send back to home page
            return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("signup.html", form = form)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


