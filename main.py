from scraper import throttle
from scraper.dto.summoner_v4_by_name import SummonerApi, PlatformHost


def throttled_function(summoner_api: SummonerApi):
    summoner_name = "ravebee"
    summoner = summoner_api.request_summoner(PlatformHost.OC1, summoner_name)
    account_id = summoner.accountId


if __name__ == "__main__":
    # 20 requests every 1 second
    # 100 requests every 2 minutes
    # = 100 requests every 120 seconds
    # = 0.83
    api_key = "RGAPI-599e2736-e098-49fd-9962-be5fa67defda"
    summoner_api = SummonerApi(api_key)
    throttle.throttle_executions(throttled_function, summoner_api, 0.83, 5)
