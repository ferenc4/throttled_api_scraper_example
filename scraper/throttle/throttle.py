import requests
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=20, period=1)
@limits(calls=100, period=2 * 60)
def get_req(url, params=None, **kwargs):
    return requests.get(url, params, kwargs)
