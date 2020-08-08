#!/usr/bin/env python3

import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    utils.matrix_docker_build(
        "rope_alias",
        {
            "bullseye": {"base_image": "debian:bullseye-slim", "gcc_version": "10", "ncurses_version": "6", "py_version": "3.8"},
            "bionic": {"base_image": "ubuntu:bionic", "gcc_version": "8", "ncurses_version": "5", "py_version": "3.6"},
        },
        {},
        ["libstdcpp-dev", "libncurses", "libpython3"],
    )


if __name__ == "__main__":
    main()
