from prefect import flow, task, get_run_logger

@task
def print_task():
    print("Hello world!")
    logger = get_run_logger()
    logger.info("Hello world!")

@flow
def hello_world():
    logger = get_run_logger()
    logger.info("Starting flow")
    print_task()

if __name__ == "__main__":
    hello_world()
