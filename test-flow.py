import time as ttime

import prefect
from prefect import task, Flow, Parameter
from prefect.engine import signals
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run


@task
def print_task():
    logger = prefect.context.get("logger")
    logger.info("Agent connection testing")
    # print("Agent connection testing")


@task
def simple_task():
    logger = prefect.context.get("logger")
    with open("/nsls2/data/tst/proposals/2022-2/prefect-test/test-data.txt", "w") as f:
        f.write(f"Flow test - {ttime.ctime()}")


with Flow("A") as flow1:
    print_task()
    simple_task()

