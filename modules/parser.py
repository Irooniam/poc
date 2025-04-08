import logging
logger = logging.getLogger(__name__)

class LeadsError(Exception):
    pass


def parseRequest(data):
    if "lead" not in data:
        raise LeadsError("'lead' key does not exist in posted JSON'")


    logger.info(data)

