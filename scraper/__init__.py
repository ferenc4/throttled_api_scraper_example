import logging

# todo parameterise output file
logging.basicConfig(filename='app.log', level=logging.DEBUG)
LOGGER = logging.getLogger("main_logger")
LOGGER.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
LOGGER.addHandler(ch)
