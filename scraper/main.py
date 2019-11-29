import sys

from scraper import throttle
from scraper.api import LeagueOfLegendsApi, PlatformHost


class ApiTaskContext:
    api: LeagueOfLegendsApi
    summoner_name_to_acc_id: {}
    acc_id_to_match_id: {}

    def __init__(self, task_stack, api) -> None:
        super().__init__(task_stack)
        self.api = api

    def put_acc_id(self, summoner_name, acc_id):
        self.summoner_name_to_acc_id[summoner_name] = acc_id

    def put_match_id(self, acc_id, match_id):
        match_ids: set = self.acc_id_to_match_id[acc_id]
        if match_ids is None:
            match_ids = set(match_id)
        else:
            match_ids.add(match_id)


def next_match_id(context, account_id):
    totalGames = 1
    # while
    results: []
    for match_id in results:
        saved_match_ids = context.acc_id_to_match_id[account_id]
        if saved_match_ids is not None and match_id not in saved_match_ids:
            context.put_match_id(account_id, match_id)
    return


def user_lookup(context: ApiTaskContext, summoner_name: str, host: PlatformHost):
    summoner = context.api.request_summoner(host, summoner_name)
    account_id = summoner.accountId
    context.put_acc_id(summoner_name, account_id)
    return lambda c: next_match_id(context, account_id)


if __name__ == "__main__":
    # 20 requests every 1 second
    # 100 requests every 2 minutes
    # = 100 requests every 120 seconds
    # = 0.83
    max_speed = 0.83
    log_frequency_sec: float = 5
    # Retrieve dev API key from https://developer.riotgames.com/
    api_key = sys.argv[1]
    print("Running with API key " + api_key)
    stack = [lambda c: user_lookup(c, "ravebee", PlatformHost.OC1)]
    context = ApiTaskContext(stack, LeagueOfLegendsApi(api_key))
    throttle.throttle_executions(context, max_speed, log_frequency_sec)
