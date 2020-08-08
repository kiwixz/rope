#!/usr/bin/env python3

import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    version = "1.1"
    utils.matrix_docker_build(
        "vscode_alias",
        {
            "bullseye": {"base_image": "debian:bullseye-slim"},
            "bionic": {"base_image": "ubuntu:bionic"},
        },
        {"VERSION": version},
        [f"vscode-apt-{version}"],
    )


if __name__ == "__main__":
    main()
