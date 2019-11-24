import json


# https://developer.riotgames.com/apis#summoner-v4
class SummonerDto:
    profileIconId: int
    name: str
    puuid: str
    summonerLevel: int
    revisionDate: int
    id: str
    accountId: str

    def __init__(self, dict):
        vars(self).update(dict)


def from_json(json_str: str) -> SummonerDto:
    return json.loads(json_str, object_hook=SummonerDto)
