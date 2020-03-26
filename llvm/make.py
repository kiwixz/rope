#!/usr/bin/env python3

import os
import subprocess


IMAGE_TAG_BASE = "rope_llvm"
REF = "llvmorg-10.0.0"
VERSION = "10.0.0"


DISTS = {
    "bullseye": {
        "base_image": "debian:bullseye-slim",
    },
    "bionic": {
        "base_image": "ubuntu:bionic",
    },
}


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    major = VERSION.split(".", 1)[0]

    for dist, dist_env in DISTS.items():
        dockerfile = f"build/{dist}.Dockerfile"
        os.makedirs("build", exist_ok=True)
        with open("Dockerfile") as src:
            with open(dockerfile, "w") as dst:
                data = src.read()
                for key, value in dist_env.items():
                    data = data.replace(f"{{{{{key}}}}}", value)
                dst.write(data)

        image_tag = f"{IMAGE_TAG_BASE}_{dist}"
        subprocess.check_call(
            [
                "docker",
                "build",
                "-t",
                image_tag,
                "-f",
                dockerfile,
                "--build-arg",
                f"REF={REF}",
                "--build-arg",
                f"VERSION={VERSION}",
                "--build-arg",
                f"MAJOR={major}",
                ".",
            ]
        )
        container_id = subprocess.check_output(["docker", "create", image_tag]).decode().rstrip()
        try:
            out_dir = f"build/{dist}"
            os.makedirs(out_dir, exist_ok=True)
            subprocess.check_call(["docker", "cp", f"{container_id}:/root/alacritty-{VERSION}.deb", out_dir])
        finally:
            subprocess.check_call(["docker", "rm", container_id])


if __name__ == "__main__":
    main()
