import numpy as np
import prefect
from prefect import task, Flow, Parameter
import time as ttime

from tiled.client import from_profile


@task
def print_and_sleep(iterations, sleep_length):
    # Long running task to test heartbeats
    logger = prefect.context.get("logger")
    logger.info("Starting long task")
    for i in range(int(iterations)):
        logger.info(f"Iteration number {i}")
        ttime.sleep(int(sleep_length))


with Flow("long-flow") as flow:
    iterations = Parameter("iterations", default=100)
    sleep_length = Parameter("sleep_length", default=10)
    print_and_sleep(iterations, sleep_length)
