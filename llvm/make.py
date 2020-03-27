#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    version = "10.0.0"
    major = version.split(".", 1)[0]

    utils.matrix_docker_build(
        "rope_llvm",
        {
            "bullseye": {"base_image": "debian:bullseye-slim"},
            # "bionic": {"base_image": "ubuntu:bionic"},
        },
        {"REF": "llvmorg-10.0.0", "VERSION": version, "MAJOR": major},
        [f"clang-{version}", f"clang-{major}-{version}"],
    )


if __name__ == "__main__":
    main()
