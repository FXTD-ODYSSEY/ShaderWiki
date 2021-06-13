# -*- coding: utf-8 -*-
"""
1. copy `content/files` folder into `static/files`
2. override the `houdiniwiki` repo folders
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-01-17 22:25:48"

import os
import shutil
import subprocess

DIR = os.path.dirname(__file__)
root = os.path.dirname(DIR)
content_folder = os.path.join(root, "content")
static_folder = os.path.join(root, "static")
houdiniwiki = os.path.join(root, "themes",'houdiniwiki')

def copy_files(src,dst):
    os.path.exists(dst) and shutil.rmtree(dst)
    shutil.copytree(src,dst)

def main():
    # TODO 更新 submodule 拉取最新的代码
    # subprocess.run("git submodule update --init")
    src = os.path.join(content_folder, "files")
    dst = os.path.join(static_folder, "files")
    copy_files(src,dst)
    src = os.path.join(houdiniwiki, "layouts")
    dst = os.path.join(root, "layouts")
    copy_files(src,dst)
    src = os.path.join(houdiniwiki, "assets")
    dst = os.path.join(root, "assets")
    copy_files(src,dst)
    src = os.path.join(houdiniwiki, "data")
    dst = os.path.join(root, "data")
    copy_files(src,dst)
    

if __name__ == "__main__":
    main()
