#!/usr/bin/env python3

import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils


def meta_packages(names: List[str], major: str, version: str):
    return (a for name in names for a in (f"{name}-{version}", f"{name}-{major}-{version}"))


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    version = "10.0.0"
    major = version.split(".", 1)[0]

    utils.matrix_docker_build(
        "rope_llvm",
        {
            "bullseye": {"base_image": "debian:bullseye-slim"},
            "bionic": {"base_image": "ubuntu:bionic"},
        },
        {"REF": f"llvmorg-{version}", "VERSION": version, "MAJOR": major},
        [*meta_packages(["clang", "clang-tools", "clangd"], major, version), f"lld-{version}", f"lldb-{version}"],
    )


if __name__ == "__main__":
    main()
