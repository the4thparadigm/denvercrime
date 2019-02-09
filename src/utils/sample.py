# ============ Base imports ======================
import os
import time
import json
import multiprocessing as mp
# ====== External package imports ================
# ====== Internal package imports ================
# ============== Logging  ========================
import logging
from denvercrime.src.utils.setup import setup, IndentLogger
from denvercrime.src.utils.setup import run_and_catch_exceptions
logger = IndentLogger(logging.getLogger(''), {})
# =========== Config File Loading ================
from denvercrime.src.utils.config_loader import get_config
conf  = get_config()
# ================================================


# do interesting stuff here
def main():
    logger.info("here is a logging statement")
    logger.debug("here is another")
    logger.error("oops!")


# when this script is run as the main script, it will run the main method
if __name__ == "__main__":
    script_name = os.path.basename(__file__).split(".")[0]
    setup(script_name)
    run_and_catch_exceptions(logger, main)
