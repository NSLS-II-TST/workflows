import prefect
from prefect import task, Flow, Parameter

from tiled.client import from_profile


@task
def read_data(uid):
    logger = prefect.context.get("logger")
    c = from_profile("tst")
    run = c[uid]["primary"].read()
    logger.info("Done")

with Flow("validate-data") as flow:
    uid = Parameter("uid")
    read_data(uid)

