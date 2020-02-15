"""
routes.py - maps URLs to functions

"""
from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm, LoginForm, AddressForm

# ORG CODE from models import db

app = Flask(__name__)

app.secret_key = "A00r69j/3yX R~XhH!j9N]0_X/9?rT"


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
    return render_template("about.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # check if already logged in and redirect if so
    if 'email' in session:
        return redirect(url_for('home'))

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
            session['user_name'] = str(User(form.first_name.data)) + ' ' + str(UserUser(form.last_name.data))
            # send back to home page
            return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("signup.html", form = form)


@app.route("/login", methods=["GET", "POST"])
def login():
    global USERNAME
    # check if already logged in and redirect if so
    if 'email' in session:
        return redirect(url_for("home"))

    form = LoginForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template('login.html', form = form)
        else:
            email = form.email.data
            password = form.password.data

            user = dbSession.query(User).filter_by(email = email).first()
            session['user_name'] = user.firstname + ' ' + user.lastname
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for("home"))
            else:
                return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template("login.html", form = form)


@app.route("/logout")
def logout():
    session.pop('email', None) # delete the cookie
    session.pop('user_name', None)
    return redirect(url_for('index'))


@app.route("/home")
def home():
    if 'email' not in session:
        # user not logged in send to to login page
        return redirect(url_for('login'))

    form = AddressForm()

    if request.method == 'POST':
        if form.validate() == False:
            # reload the page - try again
            return render_template("home.html", form = form)
        else:
            # get the address
            address = form.address.data
            # query for places around it

            # return the results

            pass
    elif request.method == 'GET':
        return render_template("home.html", form = form)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)


