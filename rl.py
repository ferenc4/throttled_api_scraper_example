from ratelimit import limits, sleep_and_retry

import requests

FIFTEEN_MINUTES = 900


@sleep_and_retry
@limits(calls=15, period=50)
def call_api(url):
    # response = requests.get(url)

    # if response.status_code != 200:
    #     raise Exception('API response: {}'.format(response.status_code))
    # return response
    print(url)

i = 0
while True:
    call_api("hello" + str(i))
    i += 1
