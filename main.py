import sys

from scraper.req.api import PlatformHost, LeagueOfLegendsApi
from scraper.req.flow import ApiTaskExecutor


def main(api_key: str):
    print("Running with API key " + api_key)
    users = ["WUNDER", "JANKOS", "CAPS"]#, "PERKZ"   , "MIXYX"   ,"PROMISQ"]

    executor = ApiTaskExecutor([], LeagueOfLegendsApi(api_key), PlatformHost.EUW1)
    for user in users:
        executor.push(lambda: executor.new_summoner(user))
        executor.run_all()


if __name__ == "__main__":
    # Retrieve dev API key from
    # https://developer.riotgames.com/
    api_key = sys.argv[1]
    main(api_key)
