# Proof Of Concept
This is a basic POC on how to post data to an endpoint so that it be ingested and inserted into Postgres

### Setup
Create Python virtualenv `python -m venv /path/to/new/virtual/environment`
Install packages `/path/to/new/env/bin/pip install -r requirements.txt`
Copy `sample.env` to new file called `.env`
Open up `.env` and change DB info

### Running
Running the Flask app is as simple as `/path/to/new/env/bin/python app.py`

### Creating encrypted payloads
Jump into Python shell `/path/to/new/env/bin/python`
Import the module via `from modules import crypt`
Import json module `import json`
Create a new dictionary and populate it with require fields
`data = {}
data["first_name"] = "bob"
...
...
`

The finished dictionary should look like
`{'first_name': 'bob',
 'last_name': 'someone',
 'address1': '123 happy place',
 'address2': 'suite super happy',
 'city': 'magical city',
 'zip': '99999',
 'phone': '80099999',
 'email': 'some@one.com',
 'state': 'california'}
 `

 Now you are going to encrypt this json 
 `ciphertext = crypt.encrypt(key, json.dumps(data))`

 Now just type `ciphertext` and you'll see a huge long string.  Copy that string and paste in the next curl call
 
### Making Calls
Simply curl against the endpoint `curl --header "Content-Type: application/json" -XPOST -d '{"lead": "long-encrypted-string-here"}' localhost:5000/lead`

