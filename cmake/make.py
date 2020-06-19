#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    version = "3.17.3"

    utils.matrix_docker_build(
        "rope_cmake",
        {
            "bullseye": {
                "base_image": "debian:bullseye-slim",
            },
            "bionic": {
                "base_image": "ubuntu:bionic",
            },
        },
        {"REF": f"v{version}", "VERSION": version},
        [f"cmake-{version}"],
    )


if __name__ == "__main__":
    main()
