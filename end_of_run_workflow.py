from prefect import task, flow, get_run_logger
from prefect_dask.task_runners import DaskTaskRunner
from data_validation import data_validation, read_all_streams
from  prefect2_test_flow import hello_world, print_task
# from long_flow import long_flow


@task
def log_completion():
    logger = get_run_logger()
    logger.info("Complete")


@flow(task_runner=DaskTaskRunner())
def end_of_run_workflow(stop_doc):
    uid = stop_doc["run_start"]
    # hello_world()
    print_task.submit()
    # data_validation(uid, return_state=True)
    read_all_streams.submit(uid, beamline_acronym="tst")
    # long_flow(iterations=100, sleep_length=10)
    log_completion()

