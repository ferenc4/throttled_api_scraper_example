from scraper import throttle


def throttled_function():
    print("hello")


if __name__ == "__main__":
    throttle.throttle_executions(throttled_function, 3, 5)
