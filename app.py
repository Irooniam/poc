from werkzeug.exceptions import BadRequest
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from modules import models 
from modules import parser
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


#cant do much if we dont have config file
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

# endpoint expects a base64 encoded string
@app.route("/lead", methods=["POST"])
def add_lead():
    try:
        data = request.get_json()
        lead = parser.parseRequest(data)
        logger.info(lead)
    except parser.LeadsError as e:
        return jsonify({"error": "request has error: {}".format(e)}), 400
    except BadRequest as e:
        return jsonify({"error": "request has error: {}".format(e)}), 400
    
    return jsonify({"OK": "true"}), 200 


if __name__ == '__main__':
    app.run(debug=True)
