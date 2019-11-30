import os

OUTPUT_PARENT = "out/"
if not os.path.exists(OUTPUT_PARENT):
    os.mkdir(OUTPUT_PARENT, 755)

MATCH_REFERENCE_FILE = OUTPUT_PARENT + "match_reference.csv"
SUMMONER_FILE = OUTPUT_PARENT + "summoner.csv"
MATCH_DETAIL_FILE = OUTPUT_PARENT + "match_detail.csv"
