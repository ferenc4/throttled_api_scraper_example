from scraper import throttle
from scraper.dto.summoner_v4_by_name import SummonerApi, PlatformHost
import sys


class TaskConfig:
    conf: SummonerApi

    def __init__(self, summoner_api) -> None:
        self.summoner_api = summoner_api


def throttled_function(conf: TaskConfig):
    summoner_name = "ravebee"
    summoner = conf.summoner_api.request_summoner(PlatformHost.OC1, summoner_name)
    account_id = summoner.accountId


if __name__ == "__main__":
    # 20 requests every 1 second
    # 100 requests every 2 minutes
    # = 100 requests every 120 seconds
    # = 0.83
    speed_limit = 0.83
    log_frequency_sec = 5
    # Retrieve dev API key from https://developer.riotgames.com/
    api_key = sys.argv[1]
    print("Running with API key " + api_key)
    conf = TaskConfig(SummonerApi(api_key))
    throttle.throttle_executions(throttled_function, conf, speed_limit, log_frequency_sec)
