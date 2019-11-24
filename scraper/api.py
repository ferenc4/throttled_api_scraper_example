from enum import Enum

import requests

from scraper import endpoint_summoner_v4_by_name, https_prefix
from scraper.dto.summoner_v4 import SummonerDto, from_json


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


class LeagueOfLegendsApi:
    api_key: str

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def request_summoner(self, host: PlatformHost, summoner_name: str) -> SummonerDto:
        response = requests.get(https_prefix + host.value +
                                endpoint_summoner_v4_by_name.format(summoner_name, self.api_key))
        string_contents = response.content.decode("utf-8")
        summoner: SummonerDto = from_json(string_contents)
        return summoner
