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
            "bullseye": {"base_image": "debian:bullseye-slim", "ncurses_version": "6"},
            "bionic": {"base_image": "ubuntu:bionic", "ncurses_version": "5"},
        },
        {},
        ["libncurses"],
    )


if __name__ == "__main__":
    main()
