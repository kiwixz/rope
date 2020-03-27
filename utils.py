#!/usr/bin/env python3

import os
import subprocess
from typing import Dict, List


def matrix_docker_build(
    image_tag: str, dists: Dict[str, Dict[str, str]], docker_args: Dict[str, str], packages: List[str]
):
    for dist, dist_env in dists.items():
        dockerfile = f"build/{dist}.Dockerfile"
        os.makedirs("build", exist_ok=True)
        with open("Dockerfile") as src:
            with open(dockerfile, "w") as dst:
                data = src.read()
                for key, value in dist_env.items():
                    data = data.replace(f"{{{{{key}}}}}", value)
                dst.write(data)

        image_tag_dist = f"{image_tag}_{dist}"
        subprocess.check_call(
            [
                "docker",
                "build",
                "-t",
                image_tag_dist,
                "-f",
                dockerfile,
                *[arg for key, value in docker_args.items() for arg in ["--build-arg", f"{key}={value}"]],
                ".",
            ]
        )

        container_id = subprocess.check_output(["docker", "create", image_tag_dist]).decode().rstrip()
        try:
            out_dir = f"build/{dist}"
            os.makedirs(out_dir, exist_ok=True)
            for package in packages:
                subprocess.check_call(["docker", "cp", f"{container_id}:/root/{package}.deb", out_dir])
        finally:
            subprocess.check_call(["docker", "rm", container_id])
