import time

from scraper import LOGGER


def throttle_executions(throttled: callable(None), max_invocations_per_sec: int, status_log_frequency_sec: int = None):
    start = time.time()
    last_logged = 0
    invocations = 1
    throttled()
    # avoid division by 0 if function didn't take a measurable amount of time
    avg_expected_length_sec = 1 / max_invocations_per_sec
    end = time.time()
    processing_time_sec = end - start
    if processing_time_sec == 0:
        time.sleep(avg_expected_length_sec / 2)
    while True:
        end = time.time()
        processing_time_sec = end - start

        invocations_per_sec = invocations / processing_time_sec
        if invocations_per_sec < max_invocations_per_sec:
            throttled()
            invocations += 1
        else:
            estimated_wait_time = invocations * avg_expected_length_sec - processing_time_sec
            time.sleep(estimated_wait_time)
        if status_log_frequency_sec is not None and time.time() - last_logged > status_log_frequency_sec:
            LOGGER.debug("invocations_per_sec: " + str(invocations_per_sec))
            last_logged = time.time()
