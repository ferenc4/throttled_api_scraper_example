import logging
import os

# todo parameterise output file
LOG_PARENT = 'logs/'
if not os.path.exists(LOG_PARENT):
    os.mkdir(LOG_PARENT, 755)
logging.basicConfig(filename=LOG_PARENT + 'app.log', level=logging.DEBUG)
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

endpoint_summoner_v4_by_name = "/lol/summoner/v4/summoners/by-name/{}?api_key={}"
endpoint_matchlist_v4_by_acc_id = "/lol/match/v4/matchlists/by-account/{}?endIndex={}&beginIndex={}&api_key={}"
endpoint_matches_v4_by_match_id = "/lol/match/v4/matches/{}?api_key={}"
https_prefix = "https://"
