# ============ Base imports ======================
import os
import pwd
import argparse
import traceback
import logging 
# ====== External package imports ================
# ====== Internal package imports ================
# ============== Logging  ========================
# Not applicable for this script, since it 
# doesn't directly do any logging
# =========== Config File Loading ================
# Not applicable for this script, since it's 
# being called by other scripts
# ================================================


# Logger that indents logging statements according to stacktrace depth improves readability of logging output
class IndentLogger(logging.LoggerAdapter):
    """
    use this adapter with:
        import logging
        denvercrime.src.modules.utils.setup import setup, IndentLogger
        logger = IndentLogger(logging.getLogger(''), {})

        setup("logger_name")  # Runs setup script, including setting up logger

        logger.info(...)  # logs at the info level
        logger.debug(...) # logs at the debug level
        ...
    """
    @staticmethod
    def indent():
        indentation_level = len(traceback.extract_stack())
        return indentation_level-5

    def process(self, msg, kwargs):
        return "{}{}".format('-' * self.indent() + "|", msg), kwargs

# function to run any function and catch any exceptions in the logger before raising them
def run_and_catch_exceptions(logger, f, *args, **kwargs):
    try:
        result = f(*args, **kwargs)
    except Exception as e:
        exc_info = sys.exc_info()
        logger.error("".join(traceback.format_exception(*exc_info)))
        raise e
    return result


# method run in every standalone script which sets up logging
def setup(logname):
    from denvercrime.src.utils.config_loader import get_config
    conf = get_config()
    # associate command line arguments with logging levels
    log_dict = {'debug': logging.DEBUG,
                'info': logging.INFO,
                'warning': logging.WARNING,
                'error': logging.ERROR,
                'critical': logging.CRITICAL}

    # currently parses only the logging level, but you can add more arguments as well (see python docs on logging)
    parser = argparse.ArgumentParser(usage='%(prog)s [-l]')
    parser.add_argument('-l', '--log', nargs='?', choices=log_dict.keys(), default='info', const='info',
                        help="logging level for console")
    args, extra_args = parser.parse_known_args()

    # create logging file if doesn't exist
    log_file_path = os.path.join(conf.dirs.logs, pwd.getpwuid(os.getuid())[0] + "_" + logname + ".log")
    if not os.path.exists(conf.dirs.logs):
        os.makedirs(conf.dirs.logs)
    if not os.path.exists(log_file_path):
        open(log_file_path, "w").close()

    # set up logging to file (file always does debug level)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-4s|%(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        filename=os.path.join(log_file_path),
                        filemode='a')
    # set up logging to console (only do this if there are no handlers)
    if len(logging.getLogger('').handlers) < 2:
        console = logging.StreamHandler()
        console.setLevel(log_dict[args.log])
        formatter = logging.Formatter('%(asctime)s %(levelname)-4s|%(message)s', '%Y/%m/%d %H:%M:%S')
        console.formatter = formatter
        logging.getLogger('').addHandler(console)
    logging.info("============================================================")
    return conf


# used for testing this script
def main():
    conf, confp = setup("setup_test")
    logging.info("Configuration: {}".format(conf))
    logging.error("Configuration: {}".format(confp))


if __name__ == "__main__":
    main()

