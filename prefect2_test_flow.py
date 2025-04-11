from prefect import flow, task, get_run_logger
from prefect.blocks.notifications import SlackWebhook


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
    slack_webhook_block = SlackWebhook.load("mon-prefect")
    slack_webhook_block.notify("Hello from Prefect!")

if __name__ == "__main__":
    hello_world()
