import os
import traceback

from prefect import flow, task, get_run_logger
from prefect.blocks.notifications import SlackWebhook
from prefect.context import FlowRunContext

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
        tb = traceback.format_exception_only(e)
        flow_run_name = FlowRunContext.get().flow_run.dict().get('name')
        slack_webhook_block = SlackWebhook.load("mon-prefect")
        slack_webhook_block.notify(f":bangbang: `flow-run` *{flow_run_name}* failed\n ```{tb[-1]}``` <@srx-prefect>")
        raise

if __name__ == "__main__":
    hello_world()
