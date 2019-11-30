import time

import requests
from ratelimit import limits, sleep_and_retry


# work in progress

class LimitCounter:
    max_invocations: int
    time_frame_sec: int
    invocation_count: int

    def __init__(self, max_invocations: int, time_frame_sec: int):
        self.max_invocations = max_invocations
        self.time_frame_sec = time_frame_sec
        self.invocation_count = 0

    def inc_invocations(self):
        self.invocation_count += 1


class ThrottledRequestExecutor:
    def __init__(self):
        self.limits = []
        self.start_time = None

    def __add__(self, max_invocations, time_frame_sec):
        self.limits.append(LimitCounter(max_invocations, time_frame_sec))

    def get(self, url, params=None, **kwargs):
        current_time = time.time()
        if self.start_time is None:
            self.start_time = current_time
        for limit in self.limits:
            pass
            # current_time
        return requests.get(url, params, kwargs)
