#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    version = "0.4.1"

    utils.matrix_docker_build(
        "rope_alacritty",
        {
            "bullseye": {
                "base_image": "debian:bullseye-slim",
                "apt_libs": "libexpat1-dev libfontconfig1-dev libfreetype-dev libxcb-xfixes0-dev",
            },
            "bionic": {
                "base_image": "ubuntu:bionic",
                "apt_libs": "libexpat1-dev libfontconfig1-dev libfreetype6-dev libxcb-xfixes0-dev",
            },
        },
        {"REF": f"v{version}", "VERSION": version},
        [f"alacritty-{version}"],
    )


if __name__ == "__main__":
    main()
