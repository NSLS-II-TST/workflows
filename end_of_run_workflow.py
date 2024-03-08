from prefect import task, flow, get_run_logger
# from data_validation import data_validation
from  prefect2_test_flow import hello_world
# from long_flow import long_flow


@task
def log_completion():
    logger = get_run_logger()
    logger.info("Complete")


@flow
def end_of_run_workflow(stop_doc):
    uid = stop_doc["run_start"]
    # data_validation(uid, return_state=True)
    hello_world()
    # TODO: long_flow
    log_completion()

