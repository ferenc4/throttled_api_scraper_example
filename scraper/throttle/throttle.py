import requests
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=20, period=1)
def get_req(url, params=None):
    return get_req_lim2(url, params)


@sleep_and_retry
@limits(calls=99, period=120)
def get_req_lim2(url, params):
    return requests.get(url, params)
