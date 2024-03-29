import time
from enum import Enum

from scraper import https_prefix, endpoint_summoner_v4_by_name, endpoint_matchlist_v4_by_acc_id, \
    endpoint_matches_v4_by_match_id, LOGGER
from scraper.dto import match_v4, summoner_v4
from scraper.dto.match_v4 import MatchlistDto, MatchDto
from scraper.dto.summoner_v4 import SummonerDto
from scraper.req import MATCH_DETAIL_ERROR_MSG, MATCH_LIST_ERROR_MSG, REQUEST_SUMMONER_ERROR_MSG
from scraper.throttle import throttle

REQ_LOG_MSG = "{}, api_key {} "


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
        LOGGER.info(REQ_LOG_MSG.format("request_summoner", self.api_key))
        endpoint = endpoint_summoner_v4_by_name.format(summoner_name, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        try_count = 1
        while response.status_code != 200:
            LOGGER.debug(REQUEST_SUMMONER_ERROR_MSG
                         .format(try_count, summoner_name, response.status_code, response.content))
            try_count += 1
            time.sleep(1)
            response = throttle.get_req(https_prefix + host.value + endpoint)
        string_contents = response.content.decode("utf-8")
        summoner: SummonerDto = summoner_v4.from_json(string_contents)
        return summoner

    def request_match_list(self, host: PlatformHost,
                           account_id: str,
                           begin_index: int,
                           end_index: int,
                           summoner_name: str) -> MatchlistDto:
        LOGGER.info(REQ_LOG_MSG.format("request_match_list", self.api_key))
        endpoint = endpoint_matchlist_v4_by_acc_id.format(account_id, end_index, begin_index, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        try_count = 1
        while response.status_code != 200:
            LOGGER.debug(MATCH_LIST_ERROR_MSG.format(try_count, account_id, begin_index, end_index, summoner_name,
                                                     response.status_code, response.content))
            try_count += 1
            time.sleep(1)
            response = throttle.get_req(https_prefix + host.value + endpoint)
        string_contents = response.content.decode("utf-8")
        match_list: MatchlistDto = match_v4.matchlist_from_json(string_contents)
        return match_list

    def request_match_details(self, summoner_name: str, host: PlatformHost, match_id: str) -> MatchDto:
        LOGGER.info(REQ_LOG_MSG.format("request_match_details", self.api_key))
        endpoint = endpoint_matches_v4_by_match_id.format(match_id, self.api_key)
        response = throttle.get_req(https_prefix + host.value + endpoint)
        try_count = 1
        while response.status_code != 200:
            LOGGER.debug(MATCH_DETAIL_ERROR_MSG.format(try_count, match_id, summoner_name, response.status_code,
                                                       response.content))
            try_count += 1
            time.sleep(1)
            response = throttle.get_req(https_prefix + host.value + endpoint)
        if response.status_code != 200:
            raise Exception(MATCH_DETAIL_ERROR_MSG.format(try_count, match_id, summoner_name, response.status_code,
                                                          response.content))
        string_contents = response.content.decode("utf-8")
        match: MatchDto = match_v4.match_from_json(string_contents)
        return match
