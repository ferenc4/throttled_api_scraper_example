import time

from scraper import LOGGER


class TaskContext:
    task_stack: [callable]

    def __init__(self, task_stack) -> None:
        self.task_stack = task_stack

    def push(self, task):
        self.task_stack.append(task)


def invoke_next_task(context: TaskContext):
    next_task: callable(TaskContext) = context.task_stack.pop()
    context.push(next_task(context))


def throttle_executions(context: TaskContext, max_invocations_per_sec: float,
                        status_log_frequency_sec: float = None):
    start = time.time()
    last_logged = 0
    invocations = 1
    invoke_next_task(context)
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
            invoke_next_task(context)
            invocations += 1
        else:
            estimated_wait_time = invocations * avg_expected_length_sec - processing_time_sec
            time.sleep(estimated_wait_time)
        if status_log_frequency_sec is not None and time.time() - last_logged > status_log_frequency_sec:
            LOGGER.debug("invocations_per_sec: " + str(invocations_per_sec))
            last_logged = time.time()
