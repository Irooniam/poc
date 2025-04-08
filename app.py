from flask import Flask
from dotenv import load_dotenv
from modules import models 
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


if not load_dotenv():
    exit("do not have .env file")

app = Flask(__name__)


#db config setup
connStr = "postgresql://{u}:{p}@{h}/{d}".format(
        u=os.environ["DB_USER"], 
        p=os.environ["DB_PASSWORD"], 
        h=os.environ["DB_HOST"], 
        d=os.environ["DB_NAME"]
)
app.config["SQLALCHEMY_DATABASE_URI"] = connStr 
models.db.init_app(app)

# normal we would create task to create tables once -
# not every time app starts
if models.connectDB(app) is False:
    exit("cant connect to DB. Exiting...")

@app.route("/")
def hello_world():
    return "Glorious index page"

@app.route("/lead", methods=["POST"])
def add_lead():
    return "a new lead"


if __name__ == '__main__':
    app.run(debug=True)
