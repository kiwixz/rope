#!/usr/bin/env python3

import glob
import os
import subprocess


IMAGE_TAG_BASE = "rope_alacritty"
REF = "v0.4.1"
VERSION = "0.4.1"


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    for dockerfile in glob.glob("*.Dockerfile"):
        dist = dockerfile.split(".")[0]
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
