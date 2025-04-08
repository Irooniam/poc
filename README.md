# Proof Of Concept
This is a basic POC on how to post data to an endpoint so that it be ingested and inserted into Postgres

### Setup
Create Python virtualenv `python -m venv /path/to/new/virtual/environment`
Install packages `/path/to/new/env/bin/pip install -r requirements.txt`
Copy `sample.env` to new file called `.env`
Open up `.env` and change DB info

### Running
Running the Flask app is as simple as `/path/to/new/env/bin/python app.py`

### Making Calls
Simply curl against the endpoint `curl --header "Content-Type: application/json" -XPOST -d '{"lead": "long-encrypted-string-here"}' localhost:5000/lead`

