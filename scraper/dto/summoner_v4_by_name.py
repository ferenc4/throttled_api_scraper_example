import json
from enum import Enum
from json import JSONEncoder
from collections import namedtuple
import requests

from scraper.dto import endpoint_summoner_v4_by_name, https_prefix


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


class PlatformHost(Enum):
    BR1 = "br1.api.riotgames.com"
    EUN1 = "eun1.api.riotgames.com"
    EUW1 = "euw1.api.riotgames.com"
    JP1 = "jp1.api.riotgames.com"
    KR = "kr.api.riotgames.com"
    LA1 = "la1.api.riotgames.com"
    LA2 = "la2.api.riotgames.com"
    NA1 = "na1.api.riotgames.com"
    OC1 = "oc1.api.riotgames.com"
    TR1 = "tr1.api.riotgames.com"
    RU = "ru.api.riotgames.com"


class RegionalHost(Enum):
    AMERICAS = "americas.api.riotgames.com"
    ASIA = "asia.api.riotgames.com"
    EUROPE = "europe.api.riotgames.com"


class SummonerApi:
    api_key: str

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def request_summoner(self, host: PlatformHost, summoner_name: str) -> SummonerDto:
        response = requests.get(https_prefix + host.value +
                                endpoint_summoner_v4_by_name.format(summoner_name, self.api_key))
        string_contents = response.content.decode("utf-8")
        summoner: SummonerDto = from_json(string_contents)
        return summoner
