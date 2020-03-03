#!/usr/bin/env python3


import os
import shutil
import subprocess

REF = "v1.0"
VERSION = "1.0"


def build():
    repo_dir = "build/foundry"
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
        subprocess.check_call(["git", "clone", "-b", REF, "https://github.com/kiwixz/foundry", repo_dir])
        subprocess.check_call(["./build/foundry/kiosevka/build.py"])


def package():
    root_dir = f"build/kiosevka-{VERSION}"
    if os.path.exists(root_dir):
        shutil.rmtree(root_dir)
    os.mkdir(root_dir)

    debian_dir = f"{root_dir}/DEBIAN"
    os.mkdir(debian_dir)
    with open("control") as src:
        with open(f"{debian_dir}/control", "w") as dst:
            dst.write(src.read().replace("{{version}}", VERSION))

    shutil.copytree("build/foundry/kiosevka/build/kiosevka/ttf", f"{root_dir}/usr/share/fonts/kiosevka")

    subprocess.check_call(["dpkg-deb", "-b", root_dir])


def main():
    build()
    package()


if __name__ == "__main__":
    main()
