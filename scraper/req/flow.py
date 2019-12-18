import os

from scraper.csv_tools import append_csv
from scraper.dto.match_v4 import MatchlistDto, MatchReferenceDto, MatchDto
from scraper.req import MATCH_REFERENCE_FILE, SUMMONER_FILE, MATCH_DETAIL_FILE_TEMPLATE, OUTPUT_PARENT
from scraper.req.api import LeagueOfLegendsApi, PlatformHost
from scraper.tasks import TaskExecutor
from scraper.view.match_view import match_dto_to_view


class ApiTaskExecutor(TaskExecutor):
    api: LeagueOfLegendsApi
    summoner_name_to_acc_id = {}
    acc_id_to_match_id_set = {}
    platform: PlatformHost

    def __init__(self, task_stack: [], api: LeagueOfLegendsApi, platform: PlatformHost) -> None:
        super().__init__(task_stack)
        self.api = api
        self.platform = platform

    def put_acc_id(self, summoner_name, acc_id):
        self.summoner_name_to_acc_id[summoner_name] = acc_id

    def put_match_id(self, acc_id, match_id):
        if self.acc_id_to_match_id_set.__contains__(acc_id):
            self.acc_id_to_match_id_set[acc_id].add(match_id)
        else:
            match_id_set = set()
            match_id_set.add(match_id)
            self.acc_id_to_match_id_set.__setitem__(acc_id, match_id_set)

    # add as task
    def new_summoner(self, summoner_name: str):
        summoner = self.api.request_summoner(self.platform, summoner_name)
        append_csv(SUMMONER_FILE, summoner.__dict__)
        acc_id = summoner.accountId
        self.put_acc_id(summoner_name, acc_id)
        self.task_stack.append(lambda: self.match_ids(summoner_name, acc_id, 0, 100))

    # add as task
    def match_ids(self, summoner_name: str, account_id: str, first: int, last: int):
        match_list = self.api.request_match_list(self.platform, account_id, first, last, summoner_name)
        matches: [MatchReferenceDto] = match_list.matches
        if match_list.endIndex < match_list.totalGames:
            start_index = match_list.endIndex
            end_index = match_list.endIndex + 100
            if end_index > match_list.totalGames:
                end_index = match_list.totalGames
            self.task_stack.append(lambda: self.match_ids(summoner_name, account_id, start_index, end_index))
        for match in matches:
            append_csv(MATCH_REFERENCE_FILE, match.__dict__)
            self.put_match_id(account_id, match.gameId)
            self.task_stack.append(lambda: self.match_details(summoner_name, match.gameId))

    def match_details(self, summoner_name: str, match_id: str):
        match: MatchDto = self.api.request_match_details(summoner_name, self.platform, match_id)
        append_csv(MATCH_DETAIL_FILE_TEMPLATE.format(summoner_name), match_dto_to_view(match))
