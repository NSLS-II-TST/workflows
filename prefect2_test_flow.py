from prefect import flow, task, get_run_logger
from prefect.blocks.notifications import SlackWebhook


@task
def print_task():
    print("Hello world!")
    logger = get_run_logger()
    logger.info("Hello world!")

@flow
def hello_world():
    try:
        logger = get_run_logger()
        logger.info("Starting flow")
        print_task()
        test_dict = dict()
        test_dict['key']  # Trying to create a key error here.
    except Exception as e:
        slack_webhook_block = SlackWebhook.load("mon-prefect")
        slack_webhook_block.notify(":bangbang:\n")

if __name__ == "__main__":
    hello_world()
