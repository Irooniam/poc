import base64
import binascii
import logging
import os
from modules import crypt
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

    return cleartext

