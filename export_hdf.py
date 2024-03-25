import os

import h5py
from tiled.client import from_uri


def get_filepath_from_run(run, stream_name):
    entry = getattr(run, stream_name)["external"].values().last()
    filepath = entry.data_sources()[0]["assets"][0]["data_uri"].replace(
        "file://localhost", ""
    )
    if not os.path.isfile(filepath):
        msg = f"{filepath!r} does not exist!"
        raise RuntimeError(msg)
    return filepath


if __name__ == "__main__":

    tiled_client = from_uri(
        "http://localhost:8000",
        api_key=os.getenv("TILED_API_KEY", ""),
        include_data_sources=True,
    )

    uid = "07dbb9ff-0dbd-46d6-86cb-5772529c0d02"
    run = tiled_client[uid]

    manta_filepath = get_filepath_from_run(run, "manta_standard_det_stream")
    panda_filepath = get_filepath_from_run(run, "panda3_standard_det_stream")

    print(f"{manta_filepath = !r}\n{panda_filepath = !r}")
