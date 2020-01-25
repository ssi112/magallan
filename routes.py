from flask import Flask, render_template
# ORG CODE from models import db

app = Flask(__name__)

# ORG CODE app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
# ORG CODE db.init_app(app)

# --------------------------------------------------
from models import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an engine that stores data in the local db file
engine = create_engine('postgresql://ssi112:madHatter@localhost:5432/learningflask')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


