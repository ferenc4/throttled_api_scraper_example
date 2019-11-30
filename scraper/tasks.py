class TaskExecutor:
    task_stack: [callable]

    def __init__(self, task_stack) -> None:
        self.task_stack = task_stack

    def push(self, task):
        self.task_stack.append(task)

    def invoke_next_task(self):
        next_task: callable = self.task_stack.pop()
        return next_task()

    def is_empty(self):
        return self.task_stack.__len__() == 0

    def run_all(self):
        while not self.is_empty():
            self.invoke_next_task()
