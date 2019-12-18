import os

OUTPUT_PARENT = "out/"
if not os.path.exists(OUTPUT_PARENT):
    os.mkdir(OUTPUT_PARENT, 755)
MATCH_DETAILS_PARENT = OUTPUT_PARENT + "match_details/"
if not os.path.exists(MATCH_DETAILS_PARENT):
    os.mkdir(MATCH_DETAILS_PARENT, 755)

MATCH_REFERENCE_FILE = OUTPUT_PARENT + "match_reference.csv"
SUMMONER_FILE = OUTPUT_PARENT + "summoner.csv"
# insert summoner name as parent
MATCH_DETAIL_FILE_TEMPLATE = MATCH_DETAILS_PARENT + "{}_match_detail.csv"

REQUEST_SUMMONER_ERROR_MSG = "Try {}: Failed to get summoner by summoner_name {}. Status code <{}> with response: {}."
MATCH_LIST_ERROR_MSG = "Try {}: Failed to get matchlist for {} from index {} to {} for summoner {}. " \
                       "Status code <{}> with response: {}."
MATCH_DETAIL_ERROR_MSG = "Try {}: Failed to get match by matchid {} for summoner {}. " \
                         "Status code <{}> with response: {}."
