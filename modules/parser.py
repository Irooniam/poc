import json
import base64
import binascii
import logging
import os
from modules import crypt
from modules import models
logger = logging.getLogger(__name__)

class LeadsError(Exception):
    pass


def parseRequest(data):
    if "lead" not in data:
        raise LeadsError("'lead' key does not exist in posted JSON'")

    #first we need to try to 64decode the lead data
    try:
        decoded = base64.b64decode(data["lead"])
    except binascii.Error as e:
        raise LeadsError("leads data is not base64 encoded with error {}".format(e))
    
    key = os.environ["SHARED_KEY"]
    #now we try to decrypt the ciphertext
    try:
        cleartext = crypt.decrypt(key, data["lead"])
        logger.info(" clear text {}".format(cleartext))
    except ValueError as e:
        raise LeadsError("unable to decrypt payload with error {}".format(e))

    #finally load the as json and make sure all keys exist
    try:
        logger.info(cleartext)
        j = json.loads(cleartext)
    except ValueError as e:
        raise LeadsError("unable to load json from cleartext error {}".format(e))

    fields=["first_name", "last_name", "address1", "address2", "city", "state", "zip", "phone","email"]
    for f in fields:
        if f not in j:
            raise LeadsError("missing required field {} in JSON".format(f))

    return j 

def addLead(data):
    lead = models.Lead(
            first_name = data["first_name"],
            last_name = data["last_name"],
            address1 = data["address1"],
            address2 = data["address2"],
            city = data["city"],
            state = data["state"],
            zip = data["zip"],
            phone = data["phone"],
            email = data["email"]
    )
    models.db.session.add(lead)
    models.db.session.commit()


