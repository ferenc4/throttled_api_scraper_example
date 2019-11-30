from enum import Enum

from scraper import https_prefix, endpoint_summoner_v4_by_name, endpoint_matchlist_v4_by_acc_id, \
    endpoint_matches_v4_by_match_id
from scraper.dto import match_v4, summoner_v4
from scraper.dto.match_v4 import MatchlistDto, MatchDto
from scraper.dto.summoner_v4 import SummonerDto
from scraper.throttle import throttle


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
        endpoint = endpoint_summoner_v4_by_name.format(summoner_name, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        if response.status_code != 200:
            raise Exception("Failed to get summoner by summoner_name {}.".format(summoner_name))
        string_contents = response.content.decode("utf-8")
        summoner: SummonerDto = summoner_v4.from_json(string_contents)
        return summoner

    def request_match_list(self, host: PlatformHost,
                           account_id: str,
                           begin_index: int,
                           end_index: int) -> MatchlistDto:
        endpoint = endpoint_matchlist_v4_by_acc_id.format(account_id, end_index, begin_index, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        if response.status_code != 200:
            raise Exception("Failed to get matchlist for {} from index {} to {}."
                            .format(account_id, begin_index, end_index))
        string_contents = response.content.decode("utf-8")
        match_list: MatchlistDto = match_v4.matchlist_from_json(string_contents)
        return match_list

    def request_match_details(self, host: PlatformHost,
                              match_id: str) -> MatchDto:
        endpoint = endpoint_matches_v4_by_match_id.format(match_id, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        if response.status_code != 200:
            raise Exception("Failed to get match by matchid {}.".format(match_id))
        string_contents = response.content.decode("utf-8")
        match: MatchDto = match_v4.match_from_json(string_contents)
        return match
