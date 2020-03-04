#!/usr/bin/env python3


import os
import shutil
import subprocess

VERSION = "1.1"


def build():
    repo_dir = "build/foundry"
    if os.path.exists(repo_dir):
        subprocess.check_call(["git", "-C", repo_dir, "fetch"])
        subprocess.check_call(["git", "-C", repo_dir, "checkout", VERSION])
    else:
        os.makedirs(repo_dir)
        subprocess.check_call(["git", "clone", "-b", VERSION, "https://github.com/kiwixz/foundry", repo_dir])

    subprocess.check_call([f"./{repo_dir}/kiosevka/make.py"])


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

    shutil.copytree("build/foundry/kiosevka/build/ttf", f"{root_dir}/usr/share/fonts/truetype/kiosevka")

    subprocess.check_call(["fakeroot", "dpkg-deb", "-b", root_dir])


def main():
    build()
    package()


if __name__ == "__main__":
    main()
